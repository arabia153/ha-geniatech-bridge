이 ZIP은 '로컬 저장소 전체' 구조입니다.

압축을 풀면 아래처럼 되어야 합니다.

repository.yaml
geniatech_dtv_bridge/
  config.yaml
  Dockerfile
  run.sh
  DOCS.md

즉, 이전처럼 app 폴더 하나만 넣는 게 아니라,
repository.yaml 이 루트에 같이 있어야 합니다.

권장 배치:
 /addons/ha_geniatech_repo/
   repository.yaml
   geniatech_dtv_bridge/
     config.yaml
     Dockerfile
     run.sh
     DOCS.md
