grammar UserAPI;

userAPI
    : 'email: ' email '\n'
      'is_active: ' is_active '\n'
      'full_name: ' full_name '\n'
      'password: ' password '\n'
      'username: ' username '\n'
      'is_superuser: ' is_superuser '\n'
      EOF;
      
email
    : '0: ' EMPTY_EMAIL 
    | '1: ' MISSING_AT 
    | '2: ' MISSING_DOMAIN 
    | '3: ' VALID_EMAIL;

EMPTY_EMAIL
    : ' ';

MISSING_AT
    : [a-zA-Z0-9._%+-]+ ' ';

MISSING_DOMAIN
    : [a-zA-Z0-9._%+-]+ '@' [a-zA-Z0-9.-]+ ' ';

VALID_EMAIL
    : [a-zA-Z0-9._%+-]+ '@' [a-zA-Z0-9.-]+ '.' ('com' | 'org');

is_active
    : '0: ' 'true' 
    | '1: ' 'false';

full_name
    : ALPHANUMERIC+;

password
    : '0: ' EMPTY_PASSWORD 
    | '1: ' ALPHANUMERIC (ALPHANUMERIC | SPECIAL_CHARACTERS)*;

EMPTY_PASSWORD
    : ' ';

username
    : '0: ' EMPTY_USERNAME 
    | '1: ' ALPHANUMERIC+;

EMPTY_USERNAME
    : ' ';

is_superuser
    : '0: ' 'true' 
    | '1: ' 'false';

ALPHANUMERIC
    : [a-zA-Z0-9]+;

SPECIAL_CHARACTERS
    : (~[a-zA-Z0-9"])+;
