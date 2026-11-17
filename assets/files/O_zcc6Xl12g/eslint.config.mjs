// 추가 자료: 강연의 실제 내부 설정이 아닌 설명용 최소 정책입니다.
export default [{
  files: ['src/product/**/*.js'],
  rules: {
    'no-restricted-imports': ['error', {
      paths: [{
        name: 'react',
        importNames: ['useEffect'],
        message: '제품 계층에서는 검토된 동기화 API를 사용하세요.'
      }],
      patterns: [{
        group: ['@main/*'],
        message: '제품 UI에서 main 계층을 직접 import할 수 없습니다.'
      }]
    }]
  }
}];
