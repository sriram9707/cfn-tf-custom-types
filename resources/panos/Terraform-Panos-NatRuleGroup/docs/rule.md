# Terraform::Panos::NatRuleGroup Rule

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#description" title="Description">Description</a>" : <i>String</i>,
    "<a href="#disabled" title="Disabled">Disabled</a>" : <i>Boolean</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#originalpacket" title="OriginalPacket">OriginalPacket</a>" : <i>[ <a href="rule-originalpacket.md">OriginalPacket</a>, ... ]</i>,
    "<a href="#translatedpacket" title="TranslatedPacket">TranslatedPacket</a>" : <i>[ <a href="rule-translatedpacket.md">TranslatedPacket</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#description" title="Description">Description</a>: <i>String</i>
<a href="#disabled" title="Disabled">Disabled</a>: <i>Boolean</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#originalpacket" title="OriginalPacket">OriginalPacket</a>: <i>
      - <a href="rule-originalpacket.md">OriginalPacket</a></i>
<a href="#translatedpacket" title="TranslatedPacket">TranslatedPacket</a>: <i>
      - <a href="rule-translatedpacket.md">TranslatedPacket</a></i>
</pre>

## Properties

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Disabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OriginalPacket

_Required_: No

_Type_: List of <a href="rule-originalpacket.md">OriginalPacket</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TranslatedPacket

_Required_: No

_Type_: List of <a href="rule-translatedpacket.md">TranslatedPacket</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
