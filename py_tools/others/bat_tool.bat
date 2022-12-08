@echo off
mode con cols=100 lines=30
TITLE  Script by Albert
color 09
echo. -----------------------------------------------------------------
echo. 欢迎！！
echo. Welcome！！
echo.
echo. 这只是py-tools的复刻版，python yyds！！！
echo. 
echo. 确认后按任意键继续...
echo. Press any key to continue...
echo. -----------------------------------------------------------------
pause >NUL 2>NUL
CLS
for /f "tokens=5" %%i in ('netstat -nao ^|find /i "listening" ^|find /i "5037"') do taskkill /f /pid %%i 
TITLE BAT-TOOLS V0.0(with python)
copy wget.exe  C:\Windows\System32\
wget https://www.python.org/ftp/python/3.10.0/python-3.10.0.exe
python-3.10.0.exe
goto MENU1

:MENU1
CLS
echo. ----------------------------------------
echo. 请输入 1 ^| 2 ^| 3 选择你需要的操作
echo. Please enter 1 ^| 2 select what you need
echo.
echo. 1. 启动 py-tools
echo.    Boot py-tools
echo.
echo. 2.  进入bat-tools
echo.    Goto bat-tools
echo.
echo. 3. 退  出
echo.    Exit
echo. ----------------------------------------

set choice=
set /p choice= 选择你的操作（Your choice）:
IF NOT "%Choice%"=="" SET Choice=%Choice:~0,1%
if /i "%choice%"=="1" goto TWRP
if /i "%choice%"=="2" goto Ori_REC
if /i "%choice%"=="3" goto EXIT
echo. 选择无效，请重新输入
echo. Choice is invalid, please enter again
echo.
goto MENU1

:TWRP
CLS
python .\py.py
goto MENU1

:Ori_REC
CLS
echo. ---------------------------------------
echo. 1.wget download
echo. 
echo. 2.display
echo. 
echo. 3.Run...
echo. 4.EXIT

set choice=
set /p choice= 选择你的操作（Your choice）:
IF NOT "%Choice%"=="" SET Choice=%Choice:~0,1%
if /i "%choice%"=="1" goto 0
if /i "%choice%"=="2" goto 2
if /i "%choice%"=="3" goto 3
if /i "%choice%"=="4" goto 4
echo. 选择无效，请重新输入
echo. Choice is invalid, please enter again
echo.
goto Ori_REC

:0
CLS
echo. ------------------------------------------------------------------------------
echo.  请键入链接
echo. ------------------------------------------------------------------------------
set url=
set /p url= :
wget -F D:\   %url%
echo.
echo. 文件在脚本所在目录，请自取。
explorer .
pause >NUL 2>NUL
goto Ori_REC

:EXIT
exit

:2
CLS
echo. ------------------------------------------------------------------------------
echo.  1.download on Internet
echo.
echo.  2.local files
echo.
echo.  3.EXIT
echo. ------------------------------------------------------------------------------
set /p choice= 选择你的操作（Your choice）:
IF NOT "%Choice%"=="" SET Choice=%Choice:~0,1%
if /i "%choice%"=="1" goto MI
if /i "%choice%"=="2" 
if /i "%choice%"=="3" goto Ori_REC

:N
echo. ------------------------------------------------------------------------------
echo.  please enter URL
echo. ------------------------------------------------------------------------------
set url2=
set /p url2= :
wget -O .\download %url2%
.\download
pause >NUL 2>NUL
goto Ori_REC


:4
goto MENU1
