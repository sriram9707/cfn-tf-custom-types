# Terraform::OCI::DatabaseExadataIormConfig

CloudFormation equivalent of oci_database_exadata_iorm_config

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OCI::DatabaseExadataIormConfig",
    "Properties" : {
        "<a href="#dbsystemid" title="DbSystemId">DbSystemId</a>" : <i>String</i>,
        "<a href="#objective" title="Objective">Objective</a>" : <i>String</i>,
        "<a href="#dbplans" title="DbPlans">DbPlans</a>" : <i>[ <a href="dbplans.md">DbPlans</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OCI::DatabaseExadataIormConfig
Properties:
    <a href="#dbsystemid" title="DbSystemId">DbSystemId</a>: <i>String</i>
    <a href="#objective" title="Objective">Objective</a>: <i>String</i>
    <a href="#dbplans" title="DbPlans">DbPlans</a>: <i>
      - <a href="dbplans.md">DbPlans</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### DbSystemId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Objective

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DbPlans

_Required_: No

_Type_: List of <a href="dbplans.md">DbPlans</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### LifecycleDetails

Returns the <code>LifecycleDetails</code> value.

#### State

Returns the <code>State</code> value.
