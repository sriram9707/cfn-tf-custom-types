# Terraform::Alicloud::DbReadWriteSplittingConnection

CloudFormation equivalent of alicloud_db_read_write_splitting_connection

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::DbReadWriteSplittingConnection",
    "Properties" : {
        "<a href="#connectionprefix" title="ConnectionPrefix">ConnectionPrefix</a>" : <i>String</i>,
        "<a href="#distributiontype" title="DistributionType">DistributionType</a>" : <i>String</i>,
        "<a href="#instanceid" title="InstanceId">InstanceId</a>" : <i>String</i>,
        "<a href="#maxdelaytime" title="MaxDelayTime">MaxDelayTime</a>" : <i>Double</i>,
        "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
        "<a href="#weight" title="Weight">Weight</a>" : <i>[ <a href="weight.md">Weight</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Alicloud::DbReadWriteSplittingConnection
Properties:
    <a href="#connectionprefix" title="ConnectionPrefix">ConnectionPrefix</a>: <i>String</i>
    <a href="#distributiontype" title="DistributionType">DistributionType</a>: <i>String</i>
    <a href="#instanceid" title="InstanceId">InstanceId</a>: <i>String</i>
    <a href="#maxdelaytime" title="MaxDelayTime">MaxDelayTime</a>: <i>Double</i>
    <a href="#port" title="Port">Port</a>: <i>Double</i>
    <a href="#weight" title="Weight">Weight</a>: <i>
      - <a href="weight.md">Weight</a></i>
</pre>

## Properties

#### ConnectionPrefix

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DistributionType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxDelayTime

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Weight

_Required_: No

_Type_: List of <a href="weight.md">Weight</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### ConnectionString

Returns the <code>ConnectionString</code> value.
