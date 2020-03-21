# Terraform::Vault::DatabaseSecretBackendConnection

CloudFormation equivalent of vault_database_secret_backend_connection

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Vault::DatabaseSecretBackendConnection",
    "Properties" : {
        "<a href="#allowedroles" title="AllowedRoles">AllowedRoles</a>" : <i>[ String, ... ]</i>,
        "<a href="#backend" title="Backend">Backend</a>" : <i>String</i>,
        "<a href="#data" title="Data">Data</a>" : <i>[ <a href="data.md">Data</a>, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#rootrotationstatements" title="RootRotationStatements">RootRotationStatements</a>" : <i>[ String, ... ]</i>,
        "<a href="#verifyconnection" title="VerifyConnection">VerifyConnection</a>" : <i>Boolean</i>,
        "<a href="#cassandra" title="Cassandra">Cassandra</a>" : <i>[ <a href="cassandra.md">Cassandra</a>, ... ]</i>,
        "<a href="#hana" title="Hana">Hana</a>" : <i>[ <a href="hana.md">Hana</a>, ... ]</i>,
        "<a href="#mongodb" title="Mongodb">Mongodb</a>" : <i>[ <a href="mongodb.md">Mongodb</a>, ... ]</i>,
        "<a href="#mssql" title="Mssql">Mssql</a>" : <i>[ <a href="mssql.md">Mssql</a>, ... ]</i>,
        "<a href="#mysql" title="Mysql">Mysql</a>" : <i>[ <a href="mysql.md">Mysql</a>, ... ]</i>,
        "<a href="#mysqlaurora" title="MysqlAurora">MysqlAurora</a>" : <i>[ <a href="mysqlaurora.md">MysqlAurora</a>, ... ]</i>,
        "<a href="#mysqllegacy" title="MysqlLegacy">MysqlLegacy</a>" : <i>[ <a href="mysqllegacy.md">MysqlLegacy</a>, ... ]</i>,
        "<a href="#mysqlrds" title="MysqlRds">MysqlRds</a>" : <i>[ <a href="mysqlrds.md">MysqlRds</a>, ... ]</i>,
        "<a href="#oracle" title="Oracle">Oracle</a>" : <i>[ <a href="oracle.md">Oracle</a>, ... ]</i>,
        "<a href="#postgresql" title="Postgresql">Postgresql</a>" : <i>[ <a href="postgresql.md">Postgresql</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Vault::DatabaseSecretBackendConnection
Properties:
    <a href="#allowedroles" title="AllowedRoles">AllowedRoles</a>: <i>
      - String</i>
    <a href="#backend" title="Backend">Backend</a>: <i>String</i>
    <a href="#data" title="Data">Data</a>: <i>
      - <a href="data.md">Data</a></i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#rootrotationstatements" title="RootRotationStatements">RootRotationStatements</a>: <i>
      - String</i>
    <a href="#verifyconnection" title="VerifyConnection">VerifyConnection</a>: <i>Boolean</i>
    <a href="#cassandra" title="Cassandra">Cassandra</a>: <i>
      - <a href="cassandra.md">Cassandra</a></i>
    <a href="#hana" title="Hana">Hana</a>: <i>
      - <a href="hana.md">Hana</a></i>
    <a href="#mongodb" title="Mongodb">Mongodb</a>: <i>
      - <a href="mongodb.md">Mongodb</a></i>
    <a href="#mssql" title="Mssql">Mssql</a>: <i>
      - <a href="mssql.md">Mssql</a></i>
    <a href="#mysql" title="Mysql">Mysql</a>: <i>
      - <a href="mysql.md">Mysql</a></i>
    <a href="#mysqlaurora" title="MysqlAurora">MysqlAurora</a>: <i>
      - <a href="mysqlaurora.md">MysqlAurora</a></i>
    <a href="#mysqllegacy" title="MysqlLegacy">MysqlLegacy</a>: <i>
      - <a href="mysqllegacy.md">MysqlLegacy</a></i>
    <a href="#mysqlrds" title="MysqlRds">MysqlRds</a>: <i>
      - <a href="mysqlrds.md">MysqlRds</a></i>
    <a href="#oracle" title="Oracle">Oracle</a>: <i>
      - <a href="oracle.md">Oracle</a></i>
    <a href="#postgresql" title="Postgresql">Postgresql</a>: <i>
      - <a href="postgresql.md">Postgresql</a></i>
</pre>

## Properties

#### AllowedRoles

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Backend

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Data

_Required_: No

_Type_: List of <a href="data.md">Data</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RootRotationStatements

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VerifyConnection

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cassandra

_Required_: No

_Type_: List of <a href="cassandra.md">Cassandra</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hana

_Required_: No

_Type_: List of <a href="hana.md">Hana</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mongodb

_Required_: No

_Type_: List of <a href="mongodb.md">Mongodb</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mssql

_Required_: No

_Type_: List of <a href="mssql.md">Mssql</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mysql

_Required_: No

_Type_: List of <a href="mysql.md">Mysql</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MysqlAurora

_Required_: No

_Type_: List of <a href="mysqlaurora.md">MysqlAurora</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MysqlLegacy

_Required_: No

_Type_: List of <a href="mysqllegacy.md">MysqlLegacy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MysqlRds

_Required_: No

_Type_: List of <a href="mysqlrds.md">MysqlRds</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Oracle

_Required_: No

_Type_: List of <a href="oracle.md">Oracle</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Postgresql

_Required_: No

_Type_: List of <a href="postgresql.md">Postgresql</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.
