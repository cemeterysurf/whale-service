# 🐳 whale-service 🐳

## Клонирование проекта

В терминале выполните следующую команду:

```
git clone https://github.com/cemeterysurf/whale-service.git
```

## Установка необходимых инструментов (для macOS)

Если у вас еще не установлен Docker, выполните следующие шаги:

### Установите Homebrew (если он не установлен):

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### Установите Docker через Homebrew:
```
brew install --cask docker
```

### Установите Git через Homebrew:
```
brew install git
```

### Запустите Docker:

После установки откройте Docker Desktop (его можно найти в Applications), дождитесь полной загрузки и убедитесь, что Docker работает.

### Запуск приложения

Перейдите в папку с проектом:

```
cd whale-service
```

### Запустите приложение с пересборкой контейнеров:

```
docker-compose up --build
```

### Откройте Swagger-документацию:
После успешного запуска API будет доступен по адресу:
👉 http://localhost:8009/docs
