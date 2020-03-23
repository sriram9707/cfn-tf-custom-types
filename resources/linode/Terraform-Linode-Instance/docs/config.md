# Terraform::Linode::Instance Config

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#comments" title="Comments">Comments</a>" : <i>String</i>,
    "<a href="#kernel" title="Kernel">Kernel</a>" : <i>String</i>,
    "<a href="#label" title="Label">Label</a>" : <i>String</i>,
    "<a href="#memorylimit" title="MemoryLimit">MemoryLimit</a>" : <i>Double</i>,
    "<a href="#rootdevice" title="RootDevice">RootDevice</a>" : <i>String</i>,
    "<a href="#runlevel" title="RunLevel">RunLevel</a>" : <i>String</i>,
    "<a href="#virtmode" title="VirtMode">VirtMode</a>" : <i>String</i>,
    "<a href="#devices" title="Devices">Devices</a>" : <i>[ <a href="config-devices.md">Devices</a>, ... ]</i>,
    "<a href="#helpers" title="Helpers">Helpers</a>" : <i>[ <a href="config-helpers.md">Helpers</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#comments" title="Comments">Comments</a>: <i>String</i>
<a href="#kernel" title="Kernel">Kernel</a>: <i>String</i>
<a href="#label" title="Label">Label</a>: <i>String</i>
<a href="#memorylimit" title="MemoryLimit">MemoryLimit</a>: <i>Double</i>
<a href="#rootdevice" title="RootDevice">RootDevice</a>: <i>String</i>
<a href="#runlevel" title="RunLevel">RunLevel</a>: <i>String</i>
<a href="#virtmode" title="VirtMode">VirtMode</a>: <i>String</i>
<a href="#devices" title="Devices">Devices</a>: <i>
      - <a href="config-devices.md">Devices</a></i>
<a href="#helpers" title="Helpers">Helpers</a>: <i>
      - <a href="config-helpers.md">Helpers</a></i>
</pre>

## Properties

#### Comments

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Kernel

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Label

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MemoryLimit

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RootDevice

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RunLevel

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Devices

_Required_: No

_Type_: List of <a href="config-devices.md">Devices</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Helpers

_Required_: No

_Type_: List of <a href="config-helpers.md">Helpers</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
