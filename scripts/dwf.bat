@echo off
setlocal

set "DIR=%~dp0"

if "%~1"=="" (
    java -cp "%DIR%dwf-cli.jar" DwfGit %*
    exit /b %errorlevel%
)

if "%~1"=="connect" (
    java -cp "%DIR%dwf-cli.jar" DwfGit %*
    exit /b %errorlevel%
)
if "%~1"=="diff" (
    java -cp "%DIR%dwf-cli.jar" DwfGit %*
    exit /b %errorlevel%
)
if "%~1"=="merge" (
    java -cp "%DIR%dwf-cli.jar" DwfGit %*
    exit /b %errorlevel%
)
if "%~1"=="mcommit" (
    java -cp "%DIR%dwf-cli.jar" DwfGit %*
    exit /b %errorlevel%
)
if "%~1"=="package" (
    java -cp "%DIR%dwf-cli.jar" DwfGit %*
    exit /b %errorlevel%
)
if "%~1"=="workspace" (
    java -cp "%DIR%dwf-cli.jar" DwfGit %*
    exit /b %errorlevel%
)

git %*
exit /b %errorlevel%
