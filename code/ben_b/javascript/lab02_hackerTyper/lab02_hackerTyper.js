
const django = ["import os", "from pathlib import Path", "BASE_DIR / 'subdir'", "BASE_DIR = Path(__file__).resolve().parent.parent", "          ", "     ", "          ", "    ",
"SECRET_KEY = 'django-insecure-05nah%n+j0f@x13ihus5g+^o_2ww0q2hkebz4b!#3v@jti3-9!'", "DEBUG = True ALLOWED_HOSTS = []", "    ", "   ", "          ", "                 ", "    ",
"See(https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/)","  ","      ", "           ", "          ", "    ", "      ", "   ", "  " , "    ", "         ", "    ",
"                                                                                                                                                                              ",
"INSTALLED_APPS = [", 'django.contrib.admin', 'django.contrib.auth', 'django.contrib.contenttypes', 'django.contrib.sessions', 'django.contrib.messages', "            ", "    ",
'django.contrib.staticfiles', 'posts.apps.PostsConfig', 'users.apps.UsersConfig', "]", "MIDDLEWARE = [", 'django.middleware.security.SecurityMiddleware', "            ", "    ",
'django.contrib.sessions.middleware.SessionMiddleware', 'django.middleware.common.CommonMiddleware', 'django.middleware.csrf.CsrfViewMiddleware', "       ", "  ", "   ", "    ",
"                                                                                                                                                                              ",
'django.contrib.auth.middleware.AuthenticationMiddleware', 'django.contrib.messages.middleware.MessageMiddleware',"  ","      ", "           ", "          ", "   ", " ", "    ",
'django.middleware.clickjacking.XFrameOptionsMiddleware', "]", "ROOT_URLCONF = 'lucid.urls'", "TEMPLATES = [",'BACKEND', ":", , "           ", "          ", "   ", " ", "     ",
'django.template.backends.django.DjangoTemplates', 'DIRS', ":", "[BASE_DIR/'templates']", 'APP_DIRS', ":", "True", 'OPTIONS', ":", 'context_processors', " ", "  ", " ", "     ",
"                                                                                                                                                                              ",
":", "[", 'django.template.context_processors.debug', 'django.template.context_processors.request', 'django.contrib.auth.context_processors.auth',  "     ", "  ", "   ", "    ",
'django.contrib.messages.context_processors.messages', "]", "]", "WSGI_APPLICATION", "=", 'lucid.wsgi.application', "# Database", "          ", "          ", "   ", " ", "    ",
"# https://docs.djangoproject.com/en/4.1/ref/settings/#databases", "DATABASES = {", 'default', ":", "{", 'ENGINE', ":", 'django.db.backends.sqlite3', "  ", "   ", "   ", "    ",
'NAME', ":", "BASE_DIR", "/", 'db.sqlite3', "}", "}", "# Password validation", "# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators", "     ", "    ",
"                                                                                                                                                                              ",
"AUTH_PASSWORD_VALIDATORS = [", "{", 'NAME', ":", 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', "}", "{", 'NAME', ":", "                 ", "    ",
'django.contrib.auth.password_validation.MinimumLengthValidator', "}", "{", 'NAME', ":", 'django.contrib.auth.password_validation.CommonPasswordValidator', "}", "{", " ", "   ",
"                                                                                                                                                                              ",
'NAME', ":", 'django.contrib.auth.password_validation.NumericPasswordValidator', "}", "]", "# Internationalization",  "# https://docs.djangoproject.com/en/4.1/topics/i18n/"," ",
"LANGUAGE_CODE =", 'en-us', "TIME_ZONE =", 'America/Los_Angeles', "USE_I18N = True", "USE_TZ = True", "# Static files (CSS, JavaScript, Images)", "                            ",
"# https://docs.djangoproject.com/en/4.1/howto/static-files/", "STATIC_URL =", 'static/', "STATICFILES_DIRS =", "[BASE_DIR /", 'static', "]", "# Default primary key field type",
"# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field", "DEFAULT_AUTO_FIELD =", 'django.db.models.BigAutoField', "       ", "                              ",
"LOGIN_REDIRECT_URL =", 'posts:home', "LOGOUT_REDIRECT_URL =", 'posts:home', "LOGIN_URL =", 'login' ]

let area = document.querySelector('#area')
let code = ""
let content = ': '
let randomNum = 0

document.body.addEventListener('keypress', keypress)

function keypress(){
    randomNum = Math.floor(Math.random() * django.length)
    console.log(django.length)
    code = django[randomNum]
    let text = document.createTextNode(code)
    area.appendChild(text)
}


// setInterval(function () {document.getElementById("area").innerHTML += "Displaying "}, 10000);

// setInterval(displayAlert, 100)

// function displayAlert(){
//     alert("ERROR");
// }


// setInterval(displaySomething, 1000)

// function displaySomething(){
//     document.getElementById("area").innerHTML += "Calling a function";
// }