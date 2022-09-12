// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package grafana

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// * [HTTP API](https://grafana.com/docs/grafana/latest/http_api/datasource_permissions/)
//
// ## Example Usage
//
// ```go
// package main
//
// import (
//
//	"github.com/lbrlabs/pulumi-grafana/sdk/go/grafana"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			team, err := grafana.NewTeam(ctx, "team", nil)
//			if err != nil {
//				return err
//			}
//			foo, err := grafana.NewDataSource(ctx, "foo", &grafana.DataSourceArgs{
//				Type: pulumi.String("cloudwatch"),
//				JsonDatas: DataSourceJsonDataArray{
//					&DataSourceJsonDataArgs{
//						DefaultRegion: pulumi.String("us-east-1"),
//						AuthType:      pulumi.String("keys"),
//					},
//				},
//				SecureJsonDatas: DataSourceSecureJsonDataArray{
//					&DataSourceSecureJsonDataArgs{
//						AccessKey: pulumi.String("123"),
//						SecretKey: pulumi.String("456"),
//					},
//				},
//			})
//			if err != nil {
//				return err
//			}
//			_, err = grafana.NewDataSourcePermission(ctx, "fooPermissions", &grafana.DataSourcePermissionArgs{
//				DatasourceId: foo.ID(),
//				Permissions: DataSourcePermissionPermissionArray{
//					&DataSourcePermissionPermissionArgs{
//						TeamId:     team.ID(),
//						Permission: pulumi.String("Query"),
//					},
//					&DataSourcePermissionPermissionArgs{
//						UserId:     pulumi.Int(3),
//						Permission: pulumi.String("Query"),
//					},
//				},
//			})
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
type DataSourcePermission struct {
	pulumi.CustomResourceState

	// ID of the datasource to apply permissions to.
	DatasourceId pulumi.IntOutput `pulumi:"datasourceId"`
	// The permission items to add/update. Items that are omitted from the list will be removed.
	Permissions DataSourcePermissionPermissionArrayOutput `pulumi:"permissions"`
}

// NewDataSourcePermission registers a new resource with the given unique name, arguments, and options.
func NewDataSourcePermission(ctx *pulumi.Context,
	name string, args *DataSourcePermissionArgs, opts ...pulumi.ResourceOption) (*DataSourcePermission, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.DatasourceId == nil {
		return nil, errors.New("invalid value for required argument 'DatasourceId'")
	}
	if args.Permissions == nil {
		return nil, errors.New("invalid value for required argument 'Permissions'")
	}
	opts = pkgResourceDefaultOpts(opts)
	var resource DataSourcePermission
	err := ctx.RegisterResource("grafana:index/dataSourcePermission:DataSourcePermission", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetDataSourcePermission gets an existing DataSourcePermission resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetDataSourcePermission(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *DataSourcePermissionState, opts ...pulumi.ResourceOption) (*DataSourcePermission, error) {
	var resource DataSourcePermission
	err := ctx.ReadResource("grafana:index/dataSourcePermission:DataSourcePermission", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering DataSourcePermission resources.
type dataSourcePermissionState struct {
	// ID of the datasource to apply permissions to.
	DatasourceId *int `pulumi:"datasourceId"`
	// The permission items to add/update. Items that are omitted from the list will be removed.
	Permissions []DataSourcePermissionPermission `pulumi:"permissions"`
}

type DataSourcePermissionState struct {
	// ID of the datasource to apply permissions to.
	DatasourceId pulumi.IntPtrInput
	// The permission items to add/update. Items that are omitted from the list will be removed.
	Permissions DataSourcePermissionPermissionArrayInput
}

func (DataSourcePermissionState) ElementType() reflect.Type {
	return reflect.TypeOf((*dataSourcePermissionState)(nil)).Elem()
}

type dataSourcePermissionArgs struct {
	// ID of the datasource to apply permissions to.
	DatasourceId int `pulumi:"datasourceId"`
	// The permission items to add/update. Items that are omitted from the list will be removed.
	Permissions []DataSourcePermissionPermission `pulumi:"permissions"`
}

// The set of arguments for constructing a DataSourcePermission resource.
type DataSourcePermissionArgs struct {
	// ID of the datasource to apply permissions to.
	DatasourceId pulumi.IntInput
	// The permission items to add/update. Items that are omitted from the list will be removed.
	Permissions DataSourcePermissionPermissionArrayInput
}

func (DataSourcePermissionArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*dataSourcePermissionArgs)(nil)).Elem()
}

type DataSourcePermissionInput interface {
	pulumi.Input

	ToDataSourcePermissionOutput() DataSourcePermissionOutput
	ToDataSourcePermissionOutputWithContext(ctx context.Context) DataSourcePermissionOutput
}

func (*DataSourcePermission) ElementType() reflect.Type {
	return reflect.TypeOf((**DataSourcePermission)(nil)).Elem()
}

func (i *DataSourcePermission) ToDataSourcePermissionOutput() DataSourcePermissionOutput {
	return i.ToDataSourcePermissionOutputWithContext(context.Background())
}

func (i *DataSourcePermission) ToDataSourcePermissionOutputWithContext(ctx context.Context) DataSourcePermissionOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DataSourcePermissionOutput)
}

// DataSourcePermissionArrayInput is an input type that accepts DataSourcePermissionArray and DataSourcePermissionArrayOutput values.
// You can construct a concrete instance of `DataSourcePermissionArrayInput` via:
//
//	DataSourcePermissionArray{ DataSourcePermissionArgs{...} }
type DataSourcePermissionArrayInput interface {
	pulumi.Input

	ToDataSourcePermissionArrayOutput() DataSourcePermissionArrayOutput
	ToDataSourcePermissionArrayOutputWithContext(context.Context) DataSourcePermissionArrayOutput
}

type DataSourcePermissionArray []DataSourcePermissionInput

func (DataSourcePermissionArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*DataSourcePermission)(nil)).Elem()
}

func (i DataSourcePermissionArray) ToDataSourcePermissionArrayOutput() DataSourcePermissionArrayOutput {
	return i.ToDataSourcePermissionArrayOutputWithContext(context.Background())
}

func (i DataSourcePermissionArray) ToDataSourcePermissionArrayOutputWithContext(ctx context.Context) DataSourcePermissionArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DataSourcePermissionArrayOutput)
}

// DataSourcePermissionMapInput is an input type that accepts DataSourcePermissionMap and DataSourcePermissionMapOutput values.
// You can construct a concrete instance of `DataSourcePermissionMapInput` via:
//
//	DataSourcePermissionMap{ "key": DataSourcePermissionArgs{...} }
type DataSourcePermissionMapInput interface {
	pulumi.Input

	ToDataSourcePermissionMapOutput() DataSourcePermissionMapOutput
	ToDataSourcePermissionMapOutputWithContext(context.Context) DataSourcePermissionMapOutput
}

type DataSourcePermissionMap map[string]DataSourcePermissionInput

func (DataSourcePermissionMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*DataSourcePermission)(nil)).Elem()
}

func (i DataSourcePermissionMap) ToDataSourcePermissionMapOutput() DataSourcePermissionMapOutput {
	return i.ToDataSourcePermissionMapOutputWithContext(context.Background())
}

func (i DataSourcePermissionMap) ToDataSourcePermissionMapOutputWithContext(ctx context.Context) DataSourcePermissionMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DataSourcePermissionMapOutput)
}

type DataSourcePermissionOutput struct{ *pulumi.OutputState }

func (DataSourcePermissionOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**DataSourcePermission)(nil)).Elem()
}

func (o DataSourcePermissionOutput) ToDataSourcePermissionOutput() DataSourcePermissionOutput {
	return o
}

func (o DataSourcePermissionOutput) ToDataSourcePermissionOutputWithContext(ctx context.Context) DataSourcePermissionOutput {
	return o
}

// ID of the datasource to apply permissions to.
func (o DataSourcePermissionOutput) DatasourceId() pulumi.IntOutput {
	return o.ApplyT(func(v *DataSourcePermission) pulumi.IntOutput { return v.DatasourceId }).(pulumi.IntOutput)
}

// The permission items to add/update. Items that are omitted from the list will be removed.
func (o DataSourcePermissionOutput) Permissions() DataSourcePermissionPermissionArrayOutput {
	return o.ApplyT(func(v *DataSourcePermission) DataSourcePermissionPermissionArrayOutput { return v.Permissions }).(DataSourcePermissionPermissionArrayOutput)
}

type DataSourcePermissionArrayOutput struct{ *pulumi.OutputState }

func (DataSourcePermissionArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*DataSourcePermission)(nil)).Elem()
}

func (o DataSourcePermissionArrayOutput) ToDataSourcePermissionArrayOutput() DataSourcePermissionArrayOutput {
	return o
}

func (o DataSourcePermissionArrayOutput) ToDataSourcePermissionArrayOutputWithContext(ctx context.Context) DataSourcePermissionArrayOutput {
	return o
}

func (o DataSourcePermissionArrayOutput) Index(i pulumi.IntInput) DataSourcePermissionOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *DataSourcePermission {
		return vs[0].([]*DataSourcePermission)[vs[1].(int)]
	}).(DataSourcePermissionOutput)
}

type DataSourcePermissionMapOutput struct{ *pulumi.OutputState }

func (DataSourcePermissionMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*DataSourcePermission)(nil)).Elem()
}

func (o DataSourcePermissionMapOutput) ToDataSourcePermissionMapOutput() DataSourcePermissionMapOutput {
	return o
}

func (o DataSourcePermissionMapOutput) ToDataSourcePermissionMapOutputWithContext(ctx context.Context) DataSourcePermissionMapOutput {
	return o
}

func (o DataSourcePermissionMapOutput) MapIndex(k pulumi.StringInput) DataSourcePermissionOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *DataSourcePermission {
		return vs[0].(map[string]*DataSourcePermission)[vs[1].(string)]
	}).(DataSourcePermissionOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*DataSourcePermissionInput)(nil)).Elem(), &DataSourcePermission{})
	pulumi.RegisterInputType(reflect.TypeOf((*DataSourcePermissionArrayInput)(nil)).Elem(), DataSourcePermissionArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*DataSourcePermissionMapInput)(nil)).Elem(), DataSourcePermissionMap{})
	pulumi.RegisterOutputType(DataSourcePermissionOutput{})
	pulumi.RegisterOutputType(DataSourcePermissionArrayOutput{})
	pulumi.RegisterOutputType(DataSourcePermissionMapOutput{})
}