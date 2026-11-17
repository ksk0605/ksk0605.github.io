// 추가 자료: 외부 접속·실제 발송 없는 유한 상태 모델. 형식 증명은 아닙니다.
import assert from 'node:assert/strict';

export function next(state, event) {
  if (event.type === 'cancel') return { kind: 'idle' };
  if (event.type === 'draft' || event.type === 'edit') {
    return { kind: 'draft', body: event.body };
  }
  if (event.type === 'approve') {
    if (state.kind !== 'draft' || state.body !== event.body) return state;
    return { kind: 'approved', body: state.body };
  }
  if (event.type === 'send') {
    if (state.kind !== 'approved') return state;
    if (event.body !== state.body) return state;
    return { kind: 'sent', body: state.body };
  }
  return state;
}

const events = [
  { type: 'cancel' },
  ...['draft', 'edit', 'approve', 'send'].flatMap(type =>
    ['A', 'B'].map(body => ({ type, body })))
];
let checked = 0;
function explore(state, approval, depth) {
  if (depth === 0) return;
  for (const event of events) {
    const result = next(state, event);
    // 별도 모니터: 수정은 승인을 무효화하며, 승인 당시 본문을 기억합니다.
    let validApproval = approval;
    if (['draft', 'edit', 'cancel'].includes(event.type)) validApproval = undefined;
    if (event.type === 'approve' && state.kind === 'draft' &&
        state.body === event.body) validApproval = event.body;
    if (result.kind === 'sent' && state.kind !== 'sent') {
      assert.equal(result.body, validApproval, '유효한 승인 없는 발송 전이');
      assert.equal(result.body, event.body, '승인한 내용과 다른 본문');
    }
    checked++;
    explore(result, validApproval, depth - 1);
  }
}
explore({ kind: 'idle' }, undefined, 5);
assert.deepEqual(next({ kind: 'approved', body: 'A' },
  { type: 'edit', body: 'B' }), { kind: 'draft', body: 'B' });
console.log(`PASS: ${checked}개 전이 검사 (이벤트 9개, 최대 길이 5)`);
console.log('범위: 작은 메모리 모델만 검사. 실제 인증·발송·병행 실행 보장은 아님.');
