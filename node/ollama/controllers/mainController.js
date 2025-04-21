// controllers/mainController.js
// Ollama Web Interface - 메인 라우터 및 API 연동

const express = require("express");
const router = express.Router();
const { exec } = require("child_process");
const fetch = require("node-fetch");
const cheerio = require("cheerio");

// 메인 페이지 렌더링
router.get("/", (req, res) => {
  res.render("index");
});

// Ollama API 연동 예시 (실제 API 연동은 추후 구현)
router.post("/api/generate", (req, res) => {
  // TODO: Ollama API 연동 및 응답 반환
  res.json({ result: "샘플 텍스트 생성 결과" });
});

// 시스템의 ollama 모델 리스트 반환
router.get("/api/models", (req, res) => {
  exec("ollama list", (error, stdout, stderr) => {
    if (error) return res.status(500).json({ error: stderr || error.message });
    // ollama list 결과 파싱 (첫 줄 헤더 제외, 빈 줄 제외, 모델명만 추출)
    const lines = stdout
      .split("\n")
      .slice(1)
      .filter((line) => line.trim());
    const models = lines.map((line) => line.split(/\s+/)[0]);
    res.json({ models });
  });
});

// 모델 다운로드 상태 SSE 스트리밍
router.post("/api/download/stream", (req, res) => {
  const { model } = req.body;
  if (!model) return res.status(400).json({ error: "모델명을 입력하세요." });
  res.setHeader("Content-Type", "text/event-stream");
  res.setHeader("Cache-Control", "no-cache");
  res.setHeader("Connection", "keep-alive");
  const child = exec(`ollama pull ${model}`);
  child.stdout.on("data", (chunk) => {
    res.write(`data: ${chunk.toString().replace(/\n/g, "\ndata: ")}\n\n`);
  });
  child.stderr.on("data", (chunk) => {
    res.write(
      `data: [stderr] ${chunk.toString().replace(/\n/g, "\ndata: ")}\n\n`
    );
  });
  child.on("close", (code) => {
    res.write(`data: [done]\n\n`);
    res.end();
  });
});

// 기존 단건 다운로드 API (호환성)
router.post("/api/download", (req, res) => {
  const { model } = req.body;
  if (!model) return res.status(400).json({ error: "모델명을 입력하세요." });
  exec(`ollama pull ${model}`, (error, stdout, stderr) => {
    if (error) {
      // 이미 존재하는 경우 등은 stderr에 메시지
      return res.status(500).json({ error: stderr || error.message });
    }
    res.json({ result: stdout.trim() });
  });
});

// 선택 모델로 질문 보내기
router.post("/api/ask", (req, res) => {
  const { model, prompt } = req.body;
  if (!model || !prompt)
    return res.status(400).json({ error: "모델과 프롬프트를 입력하세요." });
  // ollama run <모델명> --prompt "질문"
  // 최신 ollama CLI는 --prompt 플래그 대신 표준 입력 사용
  const child = exec(`ollama run ${model}`, (error, stdout, stderr) => {
    if (error) return res.status(500).json({ error: stderr || error.message });
    res.json({ result: stdout.trim().replace(/\n/g, "<br>") });
  });
  child.stdin.write(prompt + "\n");
  child.stdin.end();
});

// Ollama Hub에서 전체 모델 목록과 정보 크롤링
router.get("/api/available-models", async (req, res) => {
  try {
    const hubUrl = "https://ollama.com/library";
    const response = await fetch(hubUrl);
    const html = await response.text();
    const $ = cheerio.load(html);
    const models = [];
    // 각 모델 블록 파싱 (h2, 설명, pulls, tags, updated 등)
    $("h2").each((i, el) => {
      const name = $(el).text().trim();
      const desc = $(el).next("p").text().trim() || $(el).next().text().trim();
      let pulls = "-",
        tags = "-",
        updated = "-";
      let current = $(el).next();
      let found = 0;
      let texts = [];
      while (current.length && found < 15) {
        const txt = current.text().replace(/\s+/g, " ").trim();
        if (txt) texts.push(txt);
        current = current.next();
        found++;
      }
      const pullsIdx = texts.findIndex((t) => /Pulls/.test(t));
      if (pullsIdx > 0) pulls = texts[pullsIdx - 1];
      const tagsIdx = texts.findIndex((t) => /Tags/.test(t));
      if (tagsIdx > 0) tags = texts[tagsIdx - 1];
      const updatedIdx = texts.findIndex((t) => /Updated/.test(t));
      if (updatedIdx > -1)
        updated =
          texts[updatedIdx].replace(/Updated\s*/, "").trim() ||
          texts[updatedIdx + 1] ||
          "-";
      models.push({ name, desc, pulls, tags, updated });
    });
    res.json({ models });
  } catch (e) {
    console.error("Ollama Hub 모델 크롤링 오류:", e);
    res.status(500).json({ error: "모델 목록을 불러오지 못했습니다." });
  }
});

module.exports = router;
