const django = [
    "import ", "os \n",
    "from ", "pathlib ", "import ", "Path \n",
    " \n",
    "# ", "Build ", "paths ", "inside ", "the ", "project ", "like ", "this: ", "BASE_DIR / ", "subdir. \n",                                                                                                
    "BASE_DIR = ", "Path ", "(__file__) ", ".resolve() ", ".parent ", ".parent \n",                                                                       
    " \n",                                                                                                                                                                                                  
    "# ", "Quick-start ", "development ", "settings ", "- ", "unsuitable ", "for ", "production \n",
    "# ", "See ", "https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/ \n",
    " \n",
    "# ", "SECURITY ", "WARNING: ", "keep ", "the ", "secret ", "key ", "used ", "in ", "production ", "secret! \n",
    "SECRET_KEY = ", "'django-insecure-05nah%n+j0f@x13ihus5g+^o_2ww0q2hkebz4b!#3v@jti3-9!' \n",
    " \n",
    "# ", "SECURITY ", "WARNING: ", "don't ", "run ", "with ", "debug ", "turned ", "on ", "in ", "production! \n",
    " \n",                                                              
    " \n",
    "ALLOWED_HOSTS = [] \n",
    " \n",
    " \n",
    "# ", "Application ", "definition \n",
    " \n",
    "INSTALLED_APPS = [ \n",
    "    'django.contrib.admin', \n",
    "    'django.contrib.auth', \n",
    "    'django.contrib.contenttypes', \n",
    "    'django.contrib.sessions', \n",
    "    'django.contrib.messages', \n",
    "    'django.contrib.staticfiles', \n",
    "    'posts.apps.PostsConfig', \n",
    "    'users.apps.UsersConfig' \n",
    "] \n",
    " \n",
    "MIDDLEWARE = [ \n",
    "    'django.middleware.security.SecurityMiddleware', \n",
    "    'django.contrib.sessions.middleware.SessionMiddleware', \n",
    "    'django.middleware.common.CommonMiddleware', \n",
    "    'django.middleware.csrf.CsrfViewMiddleware', \n",
    "    'django.contrib.auth.middleware.AuthenticationMiddleware', \n",
    "    'django.contrib.messages.middleware.MessageMiddleware', \n",
    "    'django.middleware.clickjacking.XFrameOptionsMiddleware', \n",
    "] \n",
    " \n",
    "ROOT_URLCONF = ", "'lucid.urls' \n",
    " \n",
    "TEMPLATES = [ \n",
    "    { \n",
    "        'BACKEND': ", "'django.template.backends.django.DjangoTemplates', \n",
    "        'DIRS': ", "[BASE_DIR/'templates'], \n",
    "        'APP_DIRS': ", "True, \n",
    "        'OPTIONS': ", "{ \n",
    "            'context_processors': ", "[ \n",
    "                'django.template.context_processors.debug', \n",
    "                'django.template.context_processors.request', \n",
    "                'django.contrib.auth.context_processors.auth', \n",
    "                'django.contrib.messages.context_processors.messages', \n",
    "            ], \n",
    "        }, \n",
    "    }, \n",
    "] \n",
    " \n",
    "WSGI_APPLICATION = ", "'lucid.wsgi.application' \n",
    " \n",
    " \n",
    "# ", "Database \n",
    "# ", "https://docs.djangoproject.com/en/4.1/ref/settings/#databases \n",
    " \n",
    "DATABASES = { \n",
    "    'default': { \n",
    "        'ENGINE': ", "'django.db.backends.sqlite3', \n",
    "        'NAME': ", "BASE_DIR / ", "'db.sqlite3', \n",
    "    } \n",
    "} \n",
    " \n",
    "  \n",
    "# ", "Password ", "validation \n",
    "# ", "https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators \n",
    " \n",
    "AUTH_PASSWORD_VALIDATORS = [ \n",
    "    { \n",
    "        'NAME': ", "'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', \n",
    "    }, \n",
    "    { \n",
    "        'NAME': ", "'django.contrib.auth.password_validation.MinimumLengthValidator', \n",
    "    }, \n",
    "    { \n",
    "        'NAME': ", "'django.contrib.auth.password_validation.CommonPasswordValidator', \n",
    "    }, \n",
    "    { \n",
    "        'NAME': ", "'django.contrib.auth.password_validation.NumericPasswordValidator', \n",
    "    }, \n",
    "] \n",
    "  \n",
    " \n",
    "# ", "Internationalization \n",
    "# ", "https://docs.djangoproject.com/en/4.1/topics/i18n/ \n",
    " \n",
    "LANGUAGE_CODE = ", "'en-us' \n",
    " \n",
    "TIME_ZONE = ", "'America/Los_Angeles' \n",
    "  \n",
    "USE_I18N ", "= ", "True \n",
    " \n",
    "USE_TZ ", "= ", "True \n",
    " \n",
    " \n",
    "# ", "Static ", "files ", "(CSS, ", "JavaScript, ", "Images) \n",
    "# ", "https://docs.djangoproject.com/en/4.1/howto/static-files/ \n",
    " \n",
    "STATIC_URL ", "= ", "'static/' \n",
    "STATICFILES_DIRS ","= ", "[BASE_DIR ", "/ ", "'static'] \n",
    " \n",
    "# ", "Default ", "primary ", "key ", "field ", "type \n",
    "# ", "https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field  \n",
    "  \n",
    "DEFAULT_AUTO_FIELD ", "= ", "'django.db.models.BigAutoField' \n",
    " \n",
    "LOGIN_REDIRECT_URL ", "= ", "'posts:home' \n",
    "LOGOUT_REDIRECT_URL ", "= ", "'posts:home' \n",
    " \n",
    "LOGIN_URL ", "= ", "'login' \n",
    ]



let area = document.querySelector('#area')
area.value = ""
let code = ""
let content = ': '
let counter = 0

document.body.addEventListener('keypress', keypress)

function keypress(){
    code += django[counter] 
    counter ++
    if (counter === django.length){
        counter = 0
    }
    // let text = document.createTextNode(code)
    // area.appendChild(text)
    area.value = code
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