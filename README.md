# fetch_metadata_team86
A web application that allows users to upload files and extract the metadata of the files 

# Table of Content
1. <a href="#design">Design Resources</a>
2. <a href="#front_end">Front-End Documentation</a>
   - <a href="#frontend_live_link">Frontend Live Link</a>
   - <a href="#frontend_file_structure">frontend_file_structure</a>
3. <a href="#back_end">Back-End Documentation</a>
   - <a href="#live_api">Live API Details</a>
   - <a href="#Installing_API">Installing API (back-end)</a>
   - <a href="#storage_settings">Storage Settings</a>
   - <a href="#api_doc">API Endpoint Documentation</a>
   
    - <a href="#api_register">Registering New User</a>
    - <a href="#api_login">Login User</a>
    - <a href="#api_logout">Logout User</a>
    - <a href="#api_change_password">Change User Password</a>
    - <a href="#api_user_profile">Update User Profile</a>
    - <a href="#api_forgot_password">Forgot Password</a>
    
   - <a href="#api_extract_metadata">Extract MetaData Endpoints</a>
  
# Design: fetch_metadata_team86 <a name="design"></a>
- Research plan: https://docs.google.com/document/d/1ho9-msxN7DgEBDQaKtVoe83j9PgcdF4VyfP0Buu9dk0/edit?usp=sharing
- Figma file: https://www.figma.com/file/EzjbbhuIO996B5JoImNolD

All the design elements can be found in the various pages of the figma file above.
# Front-End: fetch_metadata_team86 <a name="front_end"></a>

## Front-End LIVE link <a name="frontend_live_link"></a>
https://metafetch.netlify.com

## File structure <a name="frontend_file_structure"></a>
the frontend implementation can be found in the frontend folder on our repository<br>
it is organised into the following folders and file:
- the index.html file(this is the landing page for our website).
- the assets folder(this contains all images/icons used in our website)
- the components folder(this folder has all html implementation of repeated properties of our website e.g navbar, header, it will be deleted once the site is looking great).
- the css folder (this is where all CSS files for the website are stored).
- the dashboard folder (this is where all the user's dashboard html files, the page they are redirected to after they login are stored).
- the pages folder (this is where all other html pages, apart from the landing page and the dashboard pages are stored);
- the scripts folder (this is where all the JS files used in the website are stored).

# Back-End: fetch_metadata_team86 <a name="back_end"></a>


## Live API <a name="live_api"></a>
- https://metafetch86.herokuapp.com/
- Username: pycodet1@gmail.com
- Password: ZURI_team_86
## Installing the API <a name="Installing_API"></a>

The API in a django project and can be installed or contributed to. To install:

- Start by Forking and Cloning the Repository to your machine.
- Change directory to the `/backend` folder
- **Create** and **activate** Python Virtual Environment. You can use his package [virtualenv](https://virtualenv.pypa.io/en/latest/user_guide.html)
- Database Settings: Mysql was used here, but you can use PostgreSQL also. check this guide for database seeting [here](https://docs.djangoproject.com/en/4.0/ref/databases/).

```python
## mySQL Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',
        'NAME': 'metafetch_db',
        'USER': 'zuriteam_root', # change this
        'PASSWORD': '',
        'PORT': '3305' # check the port, and change this
    }
}
```
If you have a `db.sqlite3` database, you can go along with the default database settings of django
```python
## Default SQlite Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

- Install all packages used. You can do that by running this command in the `/backend` folder
```python
pip install -r requirements.txt
```
- Debugging: A very lovely and easy to use tool was used to debug which is [sentry.io](https://sentry.io/). You can find the settings in the `settings.py` file on the project `fetch_metadata`. Comment them out if you don't want to go through process, but it is worth it.

After all packages have been installed in the active virtual environment, change your directory to the `/backend` folder and run the command
```python
python manage.py runserver
```

## Media Storage Tool <a name="storage_settings"></a>
- Cloudinary
- Documentation: [Cloundinary Documentation](https://pypi.org/project/django-cloudinary-storage/#:~:text=Django%20Cloudinary%20Storage%20is%20a,both%20media%20and%20static%20files.)


## API documentation <a name="api_doc"></a>

### Registering New User <a name="api_register"></a>

This API end-point would be used to register new users in the metafetch application and login in the user
immidiatly after registration.

- **End Point:** /api/auth/register/?username=**pycodUSERNAMEet**&email=**NAME@GMAIL.COM**&password=**PASSWORD**&confirm_password=**CONFIRM_PASSWORD**

- **Methods:** POST

- Sample Responce

```json
{
    "code": 200,
    "data": [
        {
            "user_id": 2,
            "token": "d08e094b22bbb0345b1b79b5423f1bb7fbbb59ab",
            "username": "",
            "first_name": "",
            "last_name": "",
            "email": "myname@gmail.com",
            "last_login": "2022-08-02T22:45:24.933115Z"
        }
    ]
}
```
- Optional Fields
> - `username`
> - `first_name`
> - `last_name`

- Sample Responce of stattus `400` - Bad Request
```json
{
    "username": [
        "User with this username already exist."
    ]
}
// for invalid email

{
    "email": [
        "Enter a valid email address."
    ]
}

// password validation

{
    "password": [
        "Password does not match"
    ]
}

// if a required files is not passed

{
    "confirm_password": [
        "This field is required."
    ]
}
```



- **JavaScript Code using Fetch**

```javascript

username = document.getElementById("username")
email = document.getElementById("email")
password = document.getElementById("password")
confirm_password = document.getElementById("confirm_password")


var requestOptions = {
  method: 'POST',
  redirect: 'follow'
};

fetch(`https://metafetch86.herokuapp.com/api/auth/register/?username=${username}&email=${email}&password=${password}&confirm_password=${confirm_password}`, requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

```json
{
    "username": [
        "User with this username already exist."
    ]
}
```

### Login User <a name="api_login"></a>

This end-point would be used to log in User into the application. It returns an token and the 
properties of the user who has just been logged-in.

Here, notice that the email used to register in used as the username, this is done so that 
instead of logging in with username which can be forgotten the user should use email instead as
it is designed on the official MetaFetch UI.

- **End Point:** /api/auth/login/?username=**NAME@GMAIL.COM**&password=**PASSWORD**

- **Methods:** POST

- Sample Responce

```json
{
    "code": 200,
    "data": [
        {
            "user_id": 2,
            "token": "d08e094b22bbb0345b1b79b5423f1bb7fbbb59ab",
            "username": "",
            "first_name": "",
            "last_name": "",
            "email": "myname@gmail.com",
            "last_login": "2022-08-02T22:45:24.933115Z"
        }
    ]
}
```

- **JavaScript Code using Fetch**
```javascript
email = document.getElementById("email")
password = document.getElementById("password")

var requestOptions = {
  method: 'POST',
  redirect: 'follow'
};

fetch(`https://metafetch86.herokuapp.com/api/auth/login/?username=${email}&password=${password}`, requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

### Logout User <a name="api_logout"></a>

This end-point would be used to log a User out from the application. There is nothing serious goining 
on here. The User Token must be passed along as an header to know which user wants to logout. The front-end should remove the Token from where ever it is saved on the front-end or browser when it returns a success code `200`. 

- **End Point:** /api/auth/logout/

- **Methods:** GET

- Sample Responce of stattus `200` - Success

```json
{
    "detail": "User Logged out successfully"
}
```
- Sample Responce of stattus `401` - Unautorized

```json
{
    "detail": "Authentication credentials were not provided."
}
```

- **JavaScript Code using Fetch**
```javascript
var myHeaders = new Headers();
myHeaders.append("Authorization", "token d08e094b22bbb0345b1b79b5423f1bb7fbbb59ab");

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://metafetch86.herokuapp.com/api/auth/logout/", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```


### Change User Password <a name="api_change_password"></a>

This gives an authenticated user the oppotunity to change password.

- **End Point:** api/auth/change_password/?old_password=**OLD_PASSWORD**&new_password=**NEW_PASSWORD**

- **Methods:** PUT

- Sample Responce of `200` - Success

```json
{
    "status": "success",
    "code": 200,
    "message": "Password updated successfully",
    "data": []
}
```


- Sample Responce of stattus `401` - Unautorized
```json
{
    "detail": "Authentication credentials were not provided."
}
```
- Sample Responce of stattus `400` - Bad Request

```json
{
    "old_password": [
        "This field is required."
    ]
}
```
- JavaScript Fetch Sample Code

```javascript
var myHeaders = new Headers();
myHeaders.append("Authorization", "token d08e094b22bbb0345b1b79b5423f1bb7fbbb59ab");

var requestOptions = {
  method: 'PUT',
  headers: myHeaders,
  redirect: 'follow'
};

fetch(`https://metafetch86.herokuapp.com/api/auth/change-password/?old_password=${OLD_PASSWORD}&new_password=${NEW_PASSWORD}`, requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
### Update User Profile <a name="api_user_profile"></a>

- This gives an authenticated user the previledge to change their `first_name`, `last_name` and `email`.

- **End Point:** /api/auth/logout/

- **Methods:** PUT

- Sample Responce of stattus `200` - Success

```javascript
{
    "status": "success",
    "code": 200,
    "message": "Profile updated successfully",
    "data": [
        {
            "first_name": "myFirst",
            "last_name": "myLast",
            "email": "first@gmail.com"
        }
    ]
}
```
- Sample Responce of stattus `401` - Unautorized

```json
{
    "detail": "Authentication credentials were not provided."
}
```

- **JavaScript Code using Fetch**
```javascript
var myHeaders = new Headers();
myHeaders.append("Authorization", "token 096512768b9d6098cc7469125fdf2358673c7bc8");

var requestOptions = {
  method: 'PUT',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://metafetch86.herokuapp.com/api/auth/update_profile/?email=&first_name=taiwo&last_name=", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

### Forgot Password <a name="api_forgot_password"></a>
This operation requires 2 API endpoints, one to send a safe token to email, and the second to change password based on the token sent to email.
This gives an authenticated user the oppotunity to change password.

- **End Point:** api/auth/password_reset/

- **Methods:** POST

- Sample Responce of `200` - Success

```json
{
    "status": "OK"
}
```


- Sample Responce of stattus `401` - Unautorized
```json
{
    "detail": "Authentication credentials were not provided."
}
```
- Sample Responce of stattus `400` - Bad Request

```json
{
    "email": [
        "This field is required."
    ]
}
```
- JavaScript Fetch Sample Code

```javascript
var formdata = new FormData();
formdata.append("email", "pycodet1@gmail.com");

var requestOptions = {
  method: 'POST',
  body: formdata,
  redirect: 'follow'
};

fetch("https://metafetch86.herokuapp.com/api/auth/password_reset/", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

**Change Forgotten Password with Token sent**

- **End Point:** api/auth/password_reset/confirm/

- **Methods:** POST

- Sample Responce of `200` - Success

```json
{
    "status": "OK"
}
```

- JavaScript Fetch Sample Code

```javascript
var myHeaders = new Headers();
myHeaders.append("Authorization", "token 23c1ad67a9798aea9a6e5ed0f9a61a5cfb450689");

var formdata = new FormData();
formdata.append("file", fileInput.files[0], "/C:/Users/Adegite/Zuri training/Project Phase/fetch_metadata_team86-1/backend/modules/test_files/DSC_0911.JPG");

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  body: formdata,
  redirect: 'follow'
};

fetch("https://metafetch86.herokuapp.com/api/extract_metadata/jpg_meta_extract/", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
```
**Change Forgotten Password with Token sent**

- **End Point:** api/auth/password_reset/confirm/

- **Methods:** POST

- Sample Responce of `200` - Success

```json
{
    "status": "OK"
}
```

- Sample Responce of stattus `401` - Unautorized
```json
{
    "detail": "Authentication credentials were not provided."
}
```
- Sample Responce of stattus `400` - Bad Request

```json
{
    "old_password": [
        "This field is required."
    ]
}
```
- JavaScript Fetch Sample Code

```javascript
var formdata = new FormData();
formdata.append("token", "3339e80fe05e5ca9fc74799213f81a093d1f");
formdata.append("password", "Password@123");


var requestOptions = {
  method: 'POST',
  body: formdata,
  redirect: 'follow'
};

fetch("https://metafetch86.herokuapp.com/api/auth/password_reset/confirm/", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```


# Extract Meta Data API Endpoints <a name="api_extract_metadata"></a>

- /api/extract_metadata/image_meta_extract/
> The above end-point can be used to extract metadate from images of type 'jpeg', 'jpg', 'png', tiff only
- /api/extract_metadata/jpg_meta_extract/
> (bug) The above end-point can be used for only 'jpg' images only, it gives more details than the general `/image_meta_extract/` end-point.
- /api/extract_metadata/flat_file_metadata/
> The above end-point can be used to extract file metadata. Files of type 'doc', 'pdf', 'pptx', 'xlsx' only
- /api/extract_metadata/get_files/
> The above end-point can be used to get all the file and metadata a user has processed or saved.
- /api/extract_metadata/delete_file/{file_id}/
> The above end-point can be used to delete a particular history or file with it metadata.
- /api/extract_metadata/jpg_meta_extract/
- /api/extract_metadata/get_files/
- /api/extract_metadata/delete_file/{file_id}/


## Details
- **For IMAGES**
- Endpoint (for png, jpg, tiff): `/api/extract_metadata/image_meta_extract/`
- Special Endpoint for jpg: /api/extract_metadata/jpg_meta_extract/
- Method: GET

- JavaScript Fetch Sample Code

```javascript
var myHeaders = new Headers();
myHeaders.append("Authorization", "token 23c1ad67a9798aea9a6e5ed0f9a61a5cfb450689");

var formdata = new FormData();
formdata.append("file", fileInput.files[0], "/C:/Users/Adegite/Zuri training/Project Phase/fetch_metadata_team86-1/backend/modules/test_files/DSC_0911.JPG");

var requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: formdata,
  redirect: 'follow'
};

fetch("https://metafetch86.herokuapp.com/api/extract_metadata/image_meta_extract/", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
```


### For Flat files Metadata extraction
It is similar to images but requires an aditional parameter `file_type`, which is to be passed to the body.

**NOTE:** file_type for both docx and doc should be passed as **doc**. Others by their file extention
- **JavaScript Sample Code**
```javascript
var myHeaders = new Headers();
myHeaders.append("Authorization", "token 20de6064d30901d69e400106ad41a1f26fe9e695");

var formdata = new FormData();
formdata.append("file", fileInput.files[0], "/C:/Users/Adegite/Zuri training/Project Phase/fetch_metadata_team86-1/backend/modules/test_files/21-Day spiritual bootcamp Instructional manual.docx");
formdata.append("file_type", "doc");

var requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: formdata,
  redirect: 'follow'
};

fetch("https://metafetch86.herokuapp.com/api/extract_metadata/flat_file_metadata/", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

- **Get all document associated to the current User**
- Endpoint: /api/extract_metadata/get_files/

- **JavaScript Sample Code**
```javascript
var myHeaders = new Headers();
myHeaders.append("Authorization", "token 23c1ad67a97ea9a6e5ed0f9a61a5cfb450689");

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://metafetch86.herokuapp.com/api/extract_metadata/get_files/", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

- **TO Delete a File**

- EndPoint: /api/extract_metadata/delete_file/{file_id}/
> *{file_id} should be replaced with the actual id of the file to be deleted. User can only delete files associated with them.*

- **JavaScript Sample Code**

```javascript
var myHeaders = new Headers();
myHeaders.append("Authorization", "token 23c1ad67a9798aea9a6e5ed0f9a61a5c450689");

var requestOptions = {
  method: 'DELETE',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://metafetch86.herokuapp.com/api/extract_metadata/delete_file/8/", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
The [Django documentation](https://docs.djangoproject.com/en/dev/ref/contrib/csrf/#ajax) provides more information on retrieving the CSRF token using jQuery and sending it in requests. The CSRF token is saved as a cookie called csrftoken that you can retrieve from a HTTP response, which varies depending on the language that is being used.
