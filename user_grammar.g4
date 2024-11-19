grammar UserAPI;

userAPI
    : '{' emailField ',' isActiveField ',' fullNameField ',' passwordField ',' usernameField ',' isSuperuserField '}'
    EOF
    ;

emailField
    : '"email"' ':' '"' email '"'
    ;

email
    : EMPTY_EMAIL
    | MISSING_AT
    | MISSING_DOMAIN
    | VALID_EMAIL
    ;

EMPTY_EMAIL
    : ' ';

MISSING_AT
    : [a-zA-Z0-9._%+-]+ ' ';

MISSING_DOMAIN
    : [a-zA-Z0-9._%+-]+ '@' [a-zA-Z0-9.-]+ ' ';

VALID_EMAIL
    : [a-zA-Z0-9._%+-]+ '@' [a-zA-Z0-9.-]+ '.' (COM_TLD | ORG_TLD)
    ;

COM_TLD
    : 'com'
    ;

ORG_TLD
    : 'org'
    ;

isActiveField
    : '"is_active"' ':' boolean
    ;

boolean
    : 'true' | 'false'
    ;

fullNameField
    : '"full_name"' ':' '"' fullName '"'
    ;

fullName
    : ALPHANUMERIC (ALPHANUMERIC)*
    ;

passwordField
    : '"password"' ':' '"' password '"'
    ;

password
    : EMPTY_PASSWORD
    | ALPHANUMERIC (ALPHANUMERIC | SPECIAL_CHARACTERS)*
    ;

EMPTY_PASSWORD
    : ' ';

usernameField
    : '"username"' ':' '"' username '"'
    ;

username
    : EMPTY_USERNAME
    | ALPHANUMERIC (ALPHANUMERIC)*
    ;

EMPTY_USERNAME
    : ' ';

isSuperuserField
    : '"is_superuser"' ':' boolean
    ;

ALPHANUMERIC
    : [a-zA-Z0-9]+
    ;

SPECIAL_CHARACTERS
    : (~[a-zA-Z0-9"])+
    ;

COMMA
    : ',' ;

COLON
    : ':' ;

WS
    : [ \t\r\n]+ -> skip
    ;
