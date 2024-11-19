grammar ExerciseTypesAPI;

// **********************
// Create New User
// **********************

userCreate
    : '{' emailField ',' isActiveField ',' fullNameField ',' passwordField ',' isSuperuserField '}'
    EOF;

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
    : ' '  // Empty email string
    ;

MISSING_AT
    : [a-zA-Z0-9._%+-]+ ' '  // Missing @ symbol
    ;

MISSING_DOMAIN
    : [a-zA-Z0-9._%+-]+ '@' [a-zA-Z0-9.-]+ ' '  // Missing domain part after @
    ;

VALID_EMAIL
    : [a-zA-Z0-9._%+-]+ '@' [a-zA-Z0-9.-]+ '.' 'com'  // Valid email format
    ;

isActiveField
    : '"is_active"' ':' boolean
    ;

boolean
    : 'true' | 'false'
    ;

fullNameField
    : '"full_name"' ':' '"' (fullName) '"'
    ;

fullName
    : ALPHANUMERIC (ALPHANUMERIC)*  // At least 1 alphanumeric character
    ;

passwordField
    : '"password"' ':' '"' (password) '"'
    ;

password
    : EMPTY_PASSWORD 
    | ALPHANUMERIC (ALPHANUMERIC)*  // Valid password format (alphanumeric)
    ;

EMPTY_PASSWORD
    : ' '  // Empty password
    ;

usernameField
    : '"username"' ':' '"' (username) '"'
    ;

username
    : EMPTY_USERNAME 
    | ALPHANUMERIC (ALPHANUMERIC)*  // Valid username (alphanumeric)
    ;

EMPTY_USERNAME
    : ' '  // Empty username
    ;

isSuperuserField
    : '"is_superuser"' ':' boolean
    ;


// **********************
// Create Exercise By Name
// **********************
createExerciseByName
    : (validName | invalidName)
    ;

validName
    : ALPHANUMERIC ALPHANUMERIC ALPHANUMERIC ALPHANUMERIC ALPHANUMERIC (ALPHANUMERIC)*
    ;

invalidName
    : EMPTY_STRING
    | SPECIAL_CHARACTERS
    ;


// **********************
// Basics
// **********************
ALPHANUMERIC
    : "[a-zA-Z0-9]+"
    ;

EMPTY_STRING
    : '" "'
    ;

SPECIAL_CHARACTERS
    :  (~[a-zA-Z0-9"])+
    ;

WS
    : [ \t\r\n]+ -> skip
    ;