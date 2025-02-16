# 🔍 알고리즘 스터디 자동화 시스템 (GitHub Actions 기반)
이 프로젝트는 **GitHub Actions**를 이용하여 알고리즘 스터디의 제출 여부를 자동으로 체크하고, **디스코드(Discord) 또는 메타모스트(Mattermost) 채널로 알림을 전송**하는 시스템입니다.

---

## 📌 주요 기능
- **매주 토요일 22시 (KST)** -> 이번 주 폴더명을 안내하는 리마인드 메시지 전송
- **매주 일요일 0시 (KST)** -> 지난 주 & 이번 주의 제출 여부를 체크하여 O/X 표시 후 알림 전송
- **Secrets에 Webhook URL만 등록하면 자동 작동** (추가적인 코드 수정 필요 없음)

---

## ⚠️ 필수 설정 사항
### ✅ 1. **리포지토리 이름에 'infra'를 포함하지 마세요!**
- 'infra-repo', 'infra-study' 등의 이름이 포함된 리포지토리는 **자동 체크에서 제외됩니다.**
- **자신의 깃허브 닉네임**이나 **개인 리포지토리 이름에 'infra'가 포함되지 않도록 수정**해야 합니다.

### ✅ 2. **오가나이제이션 구조 사용**
- **반드시 깃허브 오가나이제이션을 생성**한 뒤, 각 스터디원(멤버)의 리포지토리를 **오가나이제이션 내부**에 두어야 합니다.
- 이 때, 각 리포지토리의 name은 스터디원(멤버)의 깃허브 닉네임으로 설정합니다.

### ✅ 3. **GitHub Secrests 등록 (Discord 또는 Mattermost)**
- 이 시스템은 **Discord 또는 Mattermost 웹훅(Webhook) URL이 등록되었을 때만 작동합니다.**
- 웹훅 URL이 없는 경우 자동 체크가 실행되지만, **메시지가 전송되지 않습니다.**
- **즉, yml 파일이 있어도 Secrets을 등록하지 않으면 자동으로 메시지 전송이 비활성화됩니다.**

---

## 📝 사용 예시
<img src="https://i.imgur.com/YYRni78.jpeg" alt="리마인더 발송 예시" width="50%">
<img src="https://i.imgur.com/MfJOgC3.jpeg" alt="제출 체킹 메시지 발송 예시" width="400">

[실사용 중인 스터디](https://github.com/SSAFY-while-true)

---

## 🚀 사용 방법

### 📌 1️. 이 저장소를 **포크(Fork) 또는 클론(Clone)**
이 저장소를 자신의 깃허브 계정으로 **포크하거나 클론**하세요.
```sh
git clone https://github.com/ppower-dev/algorithm-study-auto-check.git
```

### 📌 2️. GitHub Secrets 설정
GiyHub Actions가 자동으로 체크를 수행하려면 **Secrets** 설정이 필요합니다.
#### ✅ GitHub Secrets 설정 방법
1. GitHub에서 **Settings -> Secrets and variables -> Actions** 로 이동
2. **"New repository secret"** 버튼 클릭
3. 아래 항목을 추가(필요한 플랫폼만 등록)

|Secret Name|설명|필수 여부|
|:---------|:-----|:----|
|GITHUB_TOKEN|GitHub API 접근을 위한 토큰|✅ 필수|
|DISCORD_WEBHOOK_URL|Discord 웹훅 URL|선택|
|MATTERMOST_WEBHOOK_URL|Mattermost 웹훅 URL|선택|

### 📌 3️. Discord 웹훅 설정 방법
(Discord를 사용하는 경우만 등록하세요.)
1. Discord 서버에서 **서버 설정 -> Integrations -> Sebhooks** 로 이동
2. **"Create Weebhook"** 버튼 클릭
3. **보낼 채널을 지정하고, Webhook URL을 복사**
4. GitHub에서 **Secrets (DISCORD_WEBHOOK_URL)** 에 등록

### 📌 4️. Mattermost 웹훅 설정 방법
(Mattermost를 사용하는 경우만 등록하세요.)

> [!Warning]
> Mattermost 에서 Integrations 로 접근하는 방법을 아직 찾지 못했습니다. 만약 방법을 알고 계신다면 PR 부탁드립니다🙏

1. Mattermost에서 **"Integrations" -> "Incoming Webhooks"**로 이동
2. **"Add Incoming Webhook"** 버튼 클릭
3. **Webhook을 사용할 Private 채널 선택 후 저장**
4. 생성된 **Webhok URL을 복사**
5. GitHub에서 **Secrets (MATTERMOST_WEBHOOK_URL)에 등록**

---

## ⚙️ GitHub Actions 자동 실행 방식
|실행 시간(KST) | 실행 스크립트 | 기능|
|:----|:----|:----|
|토요일 22시|reminder.py|이번 주 폴더명 안내 및 업로드 리마인드|
|일요일 0시|check_submissions.py|제출 체크 및 O/X 알림 전송|

---

## 🛠️ 추가 설정 (선택)
- 기본적으로 .py, .cpp, .java 파일이 제출 파일로 간주됩니다.
- 다른 언어를 추가하고 싶다면 check_submissions.py의 check_folder_and_files()에서 확장자 리스트를 수정하세요.
```python
if item.name.lower().endswith((".py", ".cpp", ".java", ".js", ".ts")):
```
