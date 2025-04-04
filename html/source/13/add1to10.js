// 1~10까지 합 계산
let sum=0;
for(let i=1; i<=10; i++) {
	sum += i;
}

// 합을 메시지로 전송 
postMessage(sum);
