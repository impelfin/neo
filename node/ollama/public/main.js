// public/main.js
document.addEventListener('DOMContentLoaded', function () {
  const form = document.getElementById('ask-form');
  const modelSelect = document.getElementById('model-select');
  const promptInput = document.getElementById('prompt');
  const resultDiv = document.getElementById('result');
  const logList = document.getElementById('log');
  const downloadForm = document.getElementById('download-form');
  const downloadInput = document.getElementById('download-model');
  const downloadResult = document.getElementById('download-result');

  // 모델 리스트 불러오기 함수
  function loadModels(selected) {
    modelSelect.innerHTML = '<option value="">모델 선택</option>';
    fetch('/api/models').then(res => res.json()).then(data => {
      (data.models || []).forEach(model => {
        const opt = document.createElement('option');
        opt.value = model;
        opt.textContent = model;
        if (selected && model === selected) opt.selected = true;
        modelSelect.appendChild(opt);
      });
    });
  }
  loadModels();

  // Ollama Hub 전체 모델 리스트 렌더링
  const modelList = document.getElementById('model-list');
  fetch('/api/available-models')
    .then(res => res.json())
    .then(data => {
      if (!data.models) return;
      modelList.innerHTML = '';
      data.models.forEach(model => {
        // name이 없거나 빈 값인 경우 렌더링하지 않음
        if (!model.name || model.name.trim() === '') return;
        const card = document.createElement('div');
        card.className = 'model-card';
        card.innerHTML = `
          <div class="model-card-title">${model.name}</div>
          <div class="model-card-desc">${model.desc || ''}</div>
        `;

        // 카드 클릭 시 입력창에 모델명 입력
        card.addEventListener('click', () => {
          downloadInput.value = model.name;
          downloadInput.focus();
        });
        modelList.appendChild(card);
      });
    });

  // 모델 다운로드 폼 (SSE로 상태 표시)
  downloadForm.addEventListener('submit', function(e) {
    e.preventDefault();
    const modelName = downloadInput.value.trim();
    if (!modelName) return;
    downloadResult.textContent = '다운로드 중...';
    downloadResult.style.whiteSpace = 'pre-wrap';
    downloadResult.innerHTML = '';
    // SSE를 위해 XMLHttpRequest 사용
    const xhr = new XMLHttpRequest();
    xhr.open('POST', '/api/download/stream');
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function() {
      if (xhr.readyState === 3 || xhr.readyState === 4) {
        const lines = xhr.responseText.split('data: ').slice(1);
        if (lines.length) {
          // 항상 최신 메시지만 표시
          let lastLine = lines[lines.length - 1].replace(/\n/g, '').replace(/\[done\]/g, '');
          downloadResult.textContent = lastLine;
        }
        if (xhr.readyState === 4 && xhr.status === 200) {
          downloadResult.textContent += '\n[다운로드 완료]';
          loadModels(modelName + ':latest');
        }
      }
    };
    xhr.send(JSON.stringify({ model: modelName }));
    downloadInput.value = '';
  });

  form.addEventListener('submit', async function (e) {
    e.preventDefault();
    const model = modelSelect.value;
    const prompt = promptInput.value.trim();
    if (!model || !prompt) return;
    resultDiv.textContent = '로딩 중...';
    try {
      const res = await fetch('/api/ask', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ model, prompt })
      });
      const data = await res.json();
      if (data.error) throw new Error(data.error);
      resultDiv.innerHTML = data.result || '결과 없음';
      addLog('[' + model + '] 질문: ' + prompt + ' → ' + (data.result || '결과 없음'));
    } catch (err) {
      resultDiv.textContent = '에러 발생';
      addLog('에러: ' + err.message);
    }
    promptInput.value = '';
  });

  function addLog(text) {
    const li = document.createElement('li');
    li.textContent = text;
    logList.prepend(li);
  }
});
