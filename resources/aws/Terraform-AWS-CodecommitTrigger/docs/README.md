# Terraform::AWS::CodecommitTrigger

CloudFormation equivalent of aws_codecommit_trigger

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::CodecommitTrigger",
    "Properties" : {
        "<a href="#repositoryname" title="RepositoryName">RepositoryName</a>" : <i>String</i>,
        "<a href="#trigger" title="Trigger">Trigger</a>" : <i>[ <a href="trigger.md">Trigger</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::CodecommitTrigger
Properties:
    <a href="#repositoryname" title="RepositoryName">RepositoryName</a>: <i>String</i>
    <a href="#trigger" title="Trigger">Trigger</a>: <i>
      - <a href="trigger.md">Trigger</a></i>
</pre>

## Properties

#### RepositoryName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Trigger

_Required_: No

_Type_: List of <a href="trigger.md">Trigger</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### ConfigurationId

Returns the <code>ConfigurationId</code> value.

#### Id

Returns the <code>Id</code> value.
