# mygpu

NVIDIA rapidsの検証結果などの共有ページ

実験機のスペックなど
|項目|内容|備考|
|--|--|--|
|VM|Azure Standard NC4as T4 v3 (4 vcpu 数、28 GiB メモリ)||
|GPU|Nvidia Tesla T4 (1 gpu、16 GiB メモリ）||
|OS|Linux (ubuntu 24.04)||
|NVIDIAドライバ|nvidia-driver-local-repo-ubuntu2404-570.133.20_1.0-1_amd64.deb||
|Rapidsコンテナイメージ|nvcr.io/nvidia/rapidsai/notebooks:25.04-cuda12.8-py3.12||
|CUDAバージョン|12.8||
|Pythonバージョン|3.12||
|コンテナランタイム|Docker version 28.1.1||
|起動コマンド|docker run --gpus all --pull always --rm -it     --shm-size=1g --ulimit memlock=-1 --ulimit stack=67108864     -p 8888:8888 -p 8787:8787 -p 8786:8786     nvcr.io/nvidia/rapidsai/notebooks:25.04-cuda12.8-py3.12||

