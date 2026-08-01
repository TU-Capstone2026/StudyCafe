1. Windows
    * python -m venv venv_win
    * (Command Prompt) "venv_win\Scripts\activate.bat" 실행
	- PowerShell에서는 실행이 되지 않음; Command Prompt인지를 확인할 것
    * 패키지 로딩: "pip install -r requirements.txt" 시행
    * 인터피리터를 가상환경 ('venv_win':venv)의 python으로 선택

2. Mac
    * python3 -m venv venv_mac
    * 터미널에서 "source venv_mac/bin/activiate"를 실행 (가상환경 실행)
    * 패키지 로딩: "pip install -r requirements.txt" 시행
    * 인터피리터를 가상환경 ('venv_mac':venv)의 python으로 선택