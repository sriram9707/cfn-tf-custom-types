# Terraform::AWS::S3Bucket LifecycleRule

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#abortincompletemultipartuploaddays" title="AbortIncompleteMultipartUploadDays">AbortIncompleteMultipartUploadDays</a>" : <i>Double</i>,
    "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
    "<a href="#id" title="Id">Id</a>" : <i>String</i>,
    "<a href="#prefix" title="Prefix">Prefix</a>" : <i>String</i>,
    "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="lifecyclerule-tags.md">Tags</a>, ... ]</i>,
    "<a href="#expiration" title="Expiration">Expiration</a>" : <i>[ <a href="lifecyclerule-expiration.md">Expiration</a>, ... ]</i>,
    "<a href="#noncurrentversionexpiration" title="NoncurrentVersionExpiration">NoncurrentVersionExpiration</a>" : <i>[ <a href="lifecyclerule-noncurrentversionexpiration.md">NoncurrentVersionExpiration</a>, ... ]</i>,
    "<a href="#noncurrentversiontransition" title="NoncurrentVersionTransition">NoncurrentVersionTransition</a>" : <i>[ <a href="lifecyclerule-noncurrentversiontransition.md">NoncurrentVersionTransition</a>, ... ]</i>,
    "<a href="#transition" title="Transition">Transition</a>" : <i>[ <a href="lifecyclerule-transition.md">Transition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#abortincompletemultipartuploaddays" title="AbortIncompleteMultipartUploadDays">AbortIncompleteMultipartUploadDays</a>: <i>Double</i>
<a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
<a href="#id" title="Id">Id</a>: <i>String</i>
<a href="#prefix" title="Prefix">Prefix</a>: <i>String</i>
<a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="lifecyclerule-tags.md">Tags</a></i>
<a href="#expiration" title="Expiration">Expiration</a>: <i>
      - <a href="lifecyclerule-expiration.md">Expiration</a></i>
<a href="#noncurrentversionexpiration" title="NoncurrentVersionExpiration">NoncurrentVersionExpiration</a>: <i>
      - <a href="lifecyclerule-noncurrentversionexpiration.md">NoncurrentVersionExpiration</a></i>
<a href="#noncurrentversiontransition" title="NoncurrentVersionTransition">NoncurrentVersionTransition</a>: <i>
      - <a href="lifecyclerule-noncurrentversiontransition.md">NoncurrentVersionTransition</a></i>
<a href="#transition" title="Transition">Transition</a>: <i>
      - <a href="lifecyclerule-transition.md">Transition</a></i>
</pre>

## Properties

#### AbortIncompleteMultipartUploadDays

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

Specifies lifecycle rule status.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

Unique identifier for the rule.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Prefix

Object key prefix identifying one or more objects to which the rule applies.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

Specifies object tags key and value.

_Required_: No

_Type_: List of <a href="lifecyclerule-tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Expiration

_Required_: No

_Type_: List of <a href="lifecyclerule-expiration.md">Expiration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoncurrentVersionExpiration

_Required_: No

_Type_: List of <a href="lifecyclerule-noncurrentversionexpiration.md">NoncurrentVersionExpiration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoncurrentVersionTransition

_Required_: No

_Type_: List of <a href="lifecyclerule-noncurrentversiontransition.md">NoncurrentVersionTransition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Transition

_Required_: No

_Type_: List of <a href="lifecyclerule-transition.md">Transition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
