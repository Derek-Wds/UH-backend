# API documentation for Uni-Health backend

## Error messages

| Error type | Code |
| --- | --- |
| ALREADY_EXIST | `{'status': 402, 'msg': 'An user has existed.' }` |
| DOES_NOT_EXIST | `{'status': 409, 'msg': 'Does not exists.'}` |
| EMPTY | `{'status': 202, 'msg': 'None.'}` |
| HEADER_NOT_FOUND | `{'status': 999, 'msg': 'Header does not exists.'}` |
| INVALID_INPUT | `{'status': 422, 'msg': 'Invalid input.'}` |
| NO_INPUT | `{'status': 400, 'msg': 'No input data provided.'}` |
| NOT_ADMIN | `{'status': 999, 'msg': 'Admin permission denied.'}` |
| NOT_FOUND | `{'status': 404, 'msg': 'Resource could not be found.'}` |
| SERVER_ERROR | `{'status': 500, 'msg': 'An error occured.'}` |
| UNAUTHORIZED | `{'status': 401, 'msg': 'Unauthorized.'}` |
| UNKNOWN_ERROR | `{'status': 403, 'msg': 'An unknown error has occured. Please try again.' }` |

## Register API
**POST**  **/register**

### Request Value
```
{
    'username': 'test',
    'phone': '12345678',
    'password': 'test',
    'role': 'doctor' // Determine whether he/she is a doctor or patient
}
```

### Return Value
```
{
    'status': 200,
    'msg': 'Success',
    'username': 'test'
}
```
or Error Messages

<br/><br/>

## Login API
**POST** **/login**

### Request Value
```
{
    'phone': '12345678',
    'password': 'test',
    'role': 'doctor' // Determine whether he/she is a doctor or patient
}
```

### Return Value
```
{
    'status': 200,
    'msg': 'Success',
    'role': 'patient',
    'session': '12345678'
}
```
Or Error Messages

<br/><br/>

## Logout API
**GET** **/logout**

### Return Value
```
{
    'status': 200,
    'msg': 'You have been successfully logged out.'
}
```
or Error Messages


<br/><br/>

## Add Personal Data API
**POST** **/add/data**

### Request Value
```
{
    'name': 'Test',
    'email': 'test@test.com',
    'gender': 'male',
    'age': 22,
    'address': 'Century Avenue, Shanghai'
}
```

### Return Value
```
{
    'status': 200,
    'msg': 'Success',
    'role': 'patient',
    'session': '12345678'
}
```
or Error Messages

<br/><br/>

## Get Patient Personal Data API
**POST** **/get/data**

### Request Value
```
{
    'phone': '12345678'
}
```

### Return Value
```
{
    'status': 200,
    'msg': 'Success',
    'data': {
        'name': 'test',
        'email': 'test@test.com',
        'gender': 'male',
        'age': 22,
        'address': 'Century Avenue, Shanghai'
    },
    'role': 'doctor',
    'session': '11111111'
}
```
Or Error Messages

<br/><br/>

## Add Patient Log Data API
**POST** **/add/log**

### Request Value
```
{
    'title': 'Catch a cold', // Title of the log data
    'content': 'I drink a lot of water today', // Any content of the log 
    't': 'simple' // Determine whether the data is simple one or detailed one
}
```

### Return Value
```
{
    'status': 200,
    'msg': 'Success',
    'log id': 1,
    'role': 'patient',
    'session': '12345678'
}
```
or Error Messages

<br/><br/>

## Add Patient Detailed Log Data API
**POST** **/add/log**

### Request Value
```
{
    'title': 'Catch a cold', // Title of the log data
    'content': 'I drink a lot of water today', // Any content of the log 
    'date': '2019/11/10', // The appointment date with doctor
    'data': {
        'height': '178cm',
        'body temperatur': '37C'
    }, // Diseases name with details
    't': 'detailed' // Determine whether the data is simple one or detailed one
}
```

### Return Value
```
{
    'status': 200,
    'msg': 'Success',
    'log id': 1,
    'role': 'patient',
    'session': '12345678'
}
```
or Error Messages


<br/><br/>

## Get Patient Log API

### Request Value
```
{
    'phone': '12345678'
}
```

### Return Value
```
{
    'status': 200,
    'msg': 'Success',
    'data': [
        {
            'phone': '12345678',
            'name': 'test',
            'title': 'test',
            'content': 'test'
        }, {
            'phone': '12345678',
            'name': 'test',
            'title': 'test1',
            'content': 'test1',
            'date': '2019/11/10'
            'data': {
                'height': '178cm',
                'body temperatur': '37C'
            }
        }
        
    ],
    'role': 'doctor',
    'session': '11111111,
}
```
Or Error Messages

<br/><br/>

## Add Reminder To Patient API
**POST** **/add/reminder**

### Request Value
```
{
    'phone': '12345678',
    'message': 'Rememeber to take medicine today!'
}
```

### Return Value
```
{
    'status': 200,
    'msg': 'Success',
    'role': 'doctor',
    'session': '111111111'
}
```
Or Error Messages

<br/><br/>

## Add Diagnosis API
**POST** **/add/diagnosis**

### Request Value
```
{
    'phone': '12345678',
    'doctor_phone': '11111111',
    'title': 'Catch a cold', // Title of the diagnosis data
    'content': 'The patient has a fever', // Any content of the diagnosis
    'date': '2019/11/1',
    'diseases': {
        'cold': 'have a low fever for a week',
        'cough': 'have a sore throat for two days, and wants to drink water all the time'
    } // Diseases name with details
}
```

### Return Value
```
{
    'status': 200,
    'msg': 'Success',
    'diagnosis id': 1,
    'role': 'doctor',
    'session': '11111111'
}
```
Or Error Messages

<br/><br/>

## Get Diagnosis API
**POST** **/get/diagnosis**

### Request Value
```
{
    'phone': '12345678'
}
```

### Return Value
```
{
    'status': 200,
    'msg': 'Success',
    'data': [
        {
            'phone': '12345678',
            'name': 'test',
            'doctor_phone': '1111111',
            'doctor_name': 'test1',
            'title': 'test',
            'content': 'test',
            'date': '2019/11/1',
            'data': {
                'cold': 'have a low fever for a week',
                'cough': 'have a sore throat for two days, and wants to drink water all the time'
            }
        }
    ],
    'role': 'patient',
    'session': '12345678'
}
```
Or Error Messages



<br/><br/>

## Add Medicine API
**POST** **/add/medicine**

### Request Value
```
{
    'patient_phone': '12345678',
    'name': 'aspirin',
    'description': 'test',
    'times': {
        '1': '9:00 A.M.',
        '2': '12:00 P.M.',
        '3': '6:00 P.M.'
    }   
}
```

### Return Value
```
{
    'status': 200,
    'msg': 'Success',
    'role': 'doctor',
    'session': '11111111'
}
```
Or Error Messages


<br/><br/>

## Get Medicine API
**POST** **/get/medicine**

### Request Value
```
    'patient_phone': '12345678'
```

### Return Value
```
{
    'status': 200,
    'msg': 'Success',
    'data': [
        {
            'patient_phone': '12345678',
            'patient_name': 'test',
            'name': 'aspirin',
            'description': 'test',
            'times': {
                '1': '9:00 A.M.',
                '2': '12:00 P.M.',
                '3': '6:00 P.M.'
            }   
        }
    ],
    'role': 'patient',
    'session': '12345678',
}
```
Or Error Messages

<br/><br/>

## Search Patient API
**POST** **/search/patient**

### Request Value
```
{
    'phone': '12345678'
}
```

### Return Value
```
{
    'status': 200,
    'msg': 'Success',
    'data': {
        'name': 'test',
        'email': 'test@test.com',
        'gender': 'male',
        'age': 22,
        'address': 'Century Avenue'
    },
    'role': 'doctor',
    'session': '11111111'
}
```
