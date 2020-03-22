# Terraform::OCI::DatabaseDatabase Database

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#adminpassword" title="AdminPassword">AdminPassword</a>" : <i>String</i>,
    "<a href="#characterset" title="CharacterSet">CharacterSet</a>" : <i>String</i>,
    "<a href="#dbname" title="DbName">DbName</a>" : <i>String</i>,
    "<a href="#dbuniquename" title="DbUniqueName">DbUniqueName</a>" : <i>String</i>,
    "<a href="#dbworkload" title="DbWorkload">DbWorkload</a>" : <i>String</i>,
    "<a href="#definedtags" title="DefinedTags">DefinedTags</a>" : <i>[ <a href="database-definedtags.md">DefinedTags</a>, ... ]</i>,
    "<a href="#freeformtags" title="FreeformTags">FreeformTags</a>" : <i>[ <a href="database-freeformtags.md">FreeformTags</a>, ... ]</i>,
    "<a href="#ncharacterset" title="NcharacterSet">NcharacterSet</a>" : <i>String</i>,
    "<a href="#pdbname" title="PdbName">PdbName</a>" : <i>String</i>,
    "<a href="#dbbackupconfig" title="DbBackupConfig">DbBackupConfig</a>" : <i>[ <a href="database-dbbackupconfig.md">DbBackupConfig</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#adminpassword" title="AdminPassword">AdminPassword</a>: <i>String</i>
<a href="#characterset" title="CharacterSet">CharacterSet</a>: <i>String</i>
<a href="#dbname" title="DbName">DbName</a>: <i>String</i>
<a href="#dbuniquename" title="DbUniqueName">DbUniqueName</a>: <i>String</i>
<a href="#dbworkload" title="DbWorkload">DbWorkload</a>: <i>String</i>
<a href="#definedtags" title="DefinedTags">DefinedTags</a>: <i>
      - <a href="database-definedtags.md">DefinedTags</a></i>
<a href="#freeformtags" title="FreeformTags">FreeformTags</a>: <i>
      - <a href="database-freeformtags.md">FreeformTags</a></i>
<a href="#ncharacterset" title="NcharacterSet">NcharacterSet</a>: <i>String</i>
<a href="#pdbname" title="PdbName">PdbName</a>: <i>String</i>
<a href="#dbbackupconfig" title="DbBackupConfig">DbBackupConfig</a>: <i>
      - <a href="database-dbbackupconfig.md">DbBackupConfig</a></i>
</pre>

## Properties

#### AdminPassword

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CharacterSet

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DbName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DbUniqueName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DbWorkload

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefinedTags

_Required_: No

_Type_: List of <a href="database-definedtags.md">DefinedTags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FreeformTags

_Required_: No

_Type_: List of <a href="database-freeformtags.md">FreeformTags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NcharacterSet

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PdbName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DbBackupConfig

_Required_: No

_Type_: List of <a href="database-dbbackupconfig.md">DbBackupConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
