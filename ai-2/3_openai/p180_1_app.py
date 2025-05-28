from pathlib import Path

dir_path = Path('./data')

dir_path.mkdir(parents=True, exist_ok=True)

print('{0} 디렉토리 존재 여부 : {1}'.format(dir_path, dir_path.exists()))
