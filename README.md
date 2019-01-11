# timestamp-custom-resource

This example serverless application creates a custom resource that returns a timestamp as an ISO 8601 string. The timestamp is returned as an output of the template so it can be used as a nested app.

## Using the app

Since the app is intended to show an example of how custom resources can be shared via SAR and used within a SAM template via nested apps, here is an example SAM template that nests the app and stores the output timestamp in an SSM parameter:

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31

Resources:
  Timestamp:
    Type: AWS::Serverless::Application
    Properties:
      Location:
        ApplicationId: arn:aws:serverlessrepo:us-east-1:277187709615:applications/timestamp-custom-resource
        SemanticVersion: 0.0.1

  TimestampParameter:
    Type: AWS::SSM::Parameter
    Properties:
      Name: /timestamp-custom-resource/timestamp
      Type: String
      Value: !GetAtt Timestamp.Outputs.Timestamp
```

This template can be deployed using the following SAM CLI command:

```
sam deploy --template-file test/timestamp-ssm-parameter.yml --stack-name timestamp-ssm-parameter --capabilities CAPABILITY_IAM CAPABILITY_AUTO_EXPAND
```

Once the stacks have been deployed, you can check the SSM parameter value like this:

```
aws ssm get-parameters --names /timestamp-custom-resource/timestamp
```

Sample output:

```
{
    "Parameters": [
        {
            "Name": "/timestamp-custom-resource/timestamp",
            "Type": "String",
            "Value": "2019-01-11T20:10:56.269844",
            "Version": 1,
            "LastModifiedDate": 1547237466.553,
            "ARN": "arn:aws:ssm:us-east-1:012345678901:parameter/timestamp-custom-resource/timestamp"
        }
    ],
    "InvalidParameters": []
}
```

## App Parameters

1. `LogLevel` (optional) - Log level for Lambda function logging, e.g., ERROR, INFO, DEBUG, etc. Default: INFO

## App Outputs

1. `Timestamp` - ISO 8601 timestamp returned by custom resource.

## License Summary

This code is made available under the MIT license. See the LICENSE file.