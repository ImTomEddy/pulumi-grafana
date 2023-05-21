// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package grafana

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Manages Grafana library panels.
//
// * [Official documentation](https://grafana.com/docs/grafana/latest/dashboards/build-dashboards/manage-library-panels/)
// * [HTTP API](https://grafana.com/docs/grafana/latest/developers/http_api/library_element/)
//
// ## Example Usage
//
// ```go
// package main
//
// import (
//
//	"encoding/json"
//
//	"github.com/lbrlabs/pulumi-grafana/sdk/go/grafana"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			tmpJSON0, err := json.Marshal(map[string]interface{}{
//				"title":   "updated name",
//				"id":      12,
//				"version": 35,
//			})
//			if err != nil {
//				return err
//			}
//			json0 := string(tmpJSON0)
//			_, err = grafana.NewLibraryPanel(ctx, "test", &grafana.LibraryPanelArgs{
//				ModelJson: pulumi.String(json0),
//			})
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
//
// ## Import
//
// ```sh
//
//	$ pulumi import grafana:index/libraryPanel:LibraryPanel panel_name {{library_panel_slug}}
//
// ```
type LibraryPanel struct {
	pulumi.CustomResourceState

	// Timestamp when the library panel was created.
	Created pulumi.StringOutput `pulumi:"created"`
	// Numerical IDs of Grafana dashboards containing the library panel.
	DashboardIds pulumi.IntArrayOutput `pulumi:"dashboardIds"`
	// Description of the library panel.
	Description pulumi.StringOutput `pulumi:"description"`
	// ID of the folder where the library panel is stored.
	FolderId pulumi.IntPtrOutput `pulumi:"folderId"`
	// Name of the folder containing the library panel.
	FolderName pulumi.StringOutput `pulumi:"folderName"`
	// Unique ID (UID) of the folder containing the library panel.
	FolderUid pulumi.StringOutput `pulumi:"folderUid"`
	// The JSON model for the library panel.
	ModelJson pulumi.StringOutput `pulumi:"modelJson"`
	// Name of the library panel.
	Name pulumi.StringOutput `pulumi:"name"`
	// The Organization ID. If not set, the Org ID defined in the provider block will be used.
	OrgId pulumi.StringPtrOutput `pulumi:"orgId"`
	// The numeric ID of the library panel computed by Grafana.
	PanelId pulumi.IntOutput `pulumi:"panelId"`
	// Type of the library panel (eg. text).
	Type pulumi.StringOutput `pulumi:"type"`
	// The unique identifier (UID) of a library panel uniquely identifies library panels between multiple Grafana installs. It’s automatically generated unless you specify it during library panel creation.The UID provides consistent URLs for accessing library panels and when syncing library panels between multiple Grafana installs.
	Uid pulumi.StringOutput `pulumi:"uid"`
	// Timestamp when the library panel was last modified.
	Updated pulumi.StringOutput `pulumi:"updated"`
	// Version of the library panel.
	Version pulumi.IntOutput `pulumi:"version"`
}

// NewLibraryPanel registers a new resource with the given unique name, arguments, and options.
func NewLibraryPanel(ctx *pulumi.Context,
	name string, args *LibraryPanelArgs, opts ...pulumi.ResourceOption) (*LibraryPanel, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ModelJson == nil {
		return nil, errors.New("invalid value for required argument 'ModelJson'")
	}
	opts = pkgResourceDefaultOpts(opts)
	var resource LibraryPanel
	err := ctx.RegisterResource("grafana:index/libraryPanel:LibraryPanel", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetLibraryPanel gets an existing LibraryPanel resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetLibraryPanel(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *LibraryPanelState, opts ...pulumi.ResourceOption) (*LibraryPanel, error) {
	var resource LibraryPanel
	err := ctx.ReadResource("grafana:index/libraryPanel:LibraryPanel", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering LibraryPanel resources.
type libraryPanelState struct {
	// Timestamp when the library panel was created.
	Created *string `pulumi:"created"`
	// Numerical IDs of Grafana dashboards containing the library panel.
	DashboardIds []int `pulumi:"dashboardIds"`
	// Description of the library panel.
	Description *string `pulumi:"description"`
	// ID of the folder where the library panel is stored.
	FolderId *int `pulumi:"folderId"`
	// Name of the folder containing the library panel.
	FolderName *string `pulumi:"folderName"`
	// Unique ID (UID) of the folder containing the library panel.
	FolderUid *string `pulumi:"folderUid"`
	// The JSON model for the library panel.
	ModelJson *string `pulumi:"modelJson"`
	// Name of the library panel.
	Name *string `pulumi:"name"`
	// The Organization ID. If not set, the Org ID defined in the provider block will be used.
	OrgId *string `pulumi:"orgId"`
	// The numeric ID of the library panel computed by Grafana.
	PanelId *int `pulumi:"panelId"`
	// Type of the library panel (eg. text).
	Type *string `pulumi:"type"`
	// The unique identifier (UID) of a library panel uniquely identifies library panels between multiple Grafana installs. It’s automatically generated unless you specify it during library panel creation.The UID provides consistent URLs for accessing library panels and when syncing library panels between multiple Grafana installs.
	Uid *string `pulumi:"uid"`
	// Timestamp when the library panel was last modified.
	Updated *string `pulumi:"updated"`
	// Version of the library panel.
	Version *int `pulumi:"version"`
}

type LibraryPanelState struct {
	// Timestamp when the library panel was created.
	Created pulumi.StringPtrInput
	// Numerical IDs of Grafana dashboards containing the library panel.
	DashboardIds pulumi.IntArrayInput
	// Description of the library panel.
	Description pulumi.StringPtrInput
	// ID of the folder where the library panel is stored.
	FolderId pulumi.IntPtrInput
	// Name of the folder containing the library panel.
	FolderName pulumi.StringPtrInput
	// Unique ID (UID) of the folder containing the library panel.
	FolderUid pulumi.StringPtrInput
	// The JSON model for the library panel.
	ModelJson pulumi.StringPtrInput
	// Name of the library panel.
	Name pulumi.StringPtrInput
	// The Organization ID. If not set, the Org ID defined in the provider block will be used.
	OrgId pulumi.StringPtrInput
	// The numeric ID of the library panel computed by Grafana.
	PanelId pulumi.IntPtrInput
	// Type of the library panel (eg. text).
	Type pulumi.StringPtrInput
	// The unique identifier (UID) of a library panel uniquely identifies library panels between multiple Grafana installs. It’s automatically generated unless you specify it during library panel creation.The UID provides consistent URLs for accessing library panels and when syncing library panels between multiple Grafana installs.
	Uid pulumi.StringPtrInput
	// Timestamp when the library panel was last modified.
	Updated pulumi.StringPtrInput
	// Version of the library panel.
	Version pulumi.IntPtrInput
}

func (LibraryPanelState) ElementType() reflect.Type {
	return reflect.TypeOf((*libraryPanelState)(nil)).Elem()
}

type libraryPanelArgs struct {
	// ID of the folder where the library panel is stored.
	FolderId *int `pulumi:"folderId"`
	// The JSON model for the library panel.
	ModelJson string `pulumi:"modelJson"`
	// Name of the library panel.
	Name *string `pulumi:"name"`
	// The Organization ID. If not set, the Org ID defined in the provider block will be used.
	OrgId *string `pulumi:"orgId"`
	// The unique identifier (UID) of a library panel uniquely identifies library panels between multiple Grafana installs. It’s automatically generated unless you specify it during library panel creation.The UID provides consistent URLs for accessing library panels and when syncing library panels between multiple Grafana installs.
	Uid *string `pulumi:"uid"`
}

// The set of arguments for constructing a LibraryPanel resource.
type LibraryPanelArgs struct {
	// ID of the folder where the library panel is stored.
	FolderId pulumi.IntPtrInput
	// The JSON model for the library panel.
	ModelJson pulumi.StringInput
	// Name of the library panel.
	Name pulumi.StringPtrInput
	// The Organization ID. If not set, the Org ID defined in the provider block will be used.
	OrgId pulumi.StringPtrInput
	// The unique identifier (UID) of a library panel uniquely identifies library panels between multiple Grafana installs. It’s automatically generated unless you specify it during library panel creation.The UID provides consistent URLs for accessing library panels and when syncing library panels between multiple Grafana installs.
	Uid pulumi.StringPtrInput
}

func (LibraryPanelArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*libraryPanelArgs)(nil)).Elem()
}

type LibraryPanelInput interface {
	pulumi.Input

	ToLibraryPanelOutput() LibraryPanelOutput
	ToLibraryPanelOutputWithContext(ctx context.Context) LibraryPanelOutput
}

func (*LibraryPanel) ElementType() reflect.Type {
	return reflect.TypeOf((**LibraryPanel)(nil)).Elem()
}

func (i *LibraryPanel) ToLibraryPanelOutput() LibraryPanelOutput {
	return i.ToLibraryPanelOutputWithContext(context.Background())
}

func (i *LibraryPanel) ToLibraryPanelOutputWithContext(ctx context.Context) LibraryPanelOutput {
	return pulumi.ToOutputWithContext(ctx, i).(LibraryPanelOutput)
}

// LibraryPanelArrayInput is an input type that accepts LibraryPanelArray and LibraryPanelArrayOutput values.
// You can construct a concrete instance of `LibraryPanelArrayInput` via:
//
//	LibraryPanelArray{ LibraryPanelArgs{...} }
type LibraryPanelArrayInput interface {
	pulumi.Input

	ToLibraryPanelArrayOutput() LibraryPanelArrayOutput
	ToLibraryPanelArrayOutputWithContext(context.Context) LibraryPanelArrayOutput
}

type LibraryPanelArray []LibraryPanelInput

func (LibraryPanelArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*LibraryPanel)(nil)).Elem()
}

func (i LibraryPanelArray) ToLibraryPanelArrayOutput() LibraryPanelArrayOutput {
	return i.ToLibraryPanelArrayOutputWithContext(context.Background())
}

func (i LibraryPanelArray) ToLibraryPanelArrayOutputWithContext(ctx context.Context) LibraryPanelArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(LibraryPanelArrayOutput)
}

// LibraryPanelMapInput is an input type that accepts LibraryPanelMap and LibraryPanelMapOutput values.
// You can construct a concrete instance of `LibraryPanelMapInput` via:
//
//	LibraryPanelMap{ "key": LibraryPanelArgs{...} }
type LibraryPanelMapInput interface {
	pulumi.Input

	ToLibraryPanelMapOutput() LibraryPanelMapOutput
	ToLibraryPanelMapOutputWithContext(context.Context) LibraryPanelMapOutput
}

type LibraryPanelMap map[string]LibraryPanelInput

func (LibraryPanelMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*LibraryPanel)(nil)).Elem()
}

func (i LibraryPanelMap) ToLibraryPanelMapOutput() LibraryPanelMapOutput {
	return i.ToLibraryPanelMapOutputWithContext(context.Background())
}

func (i LibraryPanelMap) ToLibraryPanelMapOutputWithContext(ctx context.Context) LibraryPanelMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(LibraryPanelMapOutput)
}

type LibraryPanelOutput struct{ *pulumi.OutputState }

func (LibraryPanelOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**LibraryPanel)(nil)).Elem()
}

func (o LibraryPanelOutput) ToLibraryPanelOutput() LibraryPanelOutput {
	return o
}

func (o LibraryPanelOutput) ToLibraryPanelOutputWithContext(ctx context.Context) LibraryPanelOutput {
	return o
}

// Timestamp when the library panel was created.
func (o LibraryPanelOutput) Created() pulumi.StringOutput {
	return o.ApplyT(func(v *LibraryPanel) pulumi.StringOutput { return v.Created }).(pulumi.StringOutput)
}

// Numerical IDs of Grafana dashboards containing the library panel.
func (o LibraryPanelOutput) DashboardIds() pulumi.IntArrayOutput {
	return o.ApplyT(func(v *LibraryPanel) pulumi.IntArrayOutput { return v.DashboardIds }).(pulumi.IntArrayOutput)
}

// Description of the library panel.
func (o LibraryPanelOutput) Description() pulumi.StringOutput {
	return o.ApplyT(func(v *LibraryPanel) pulumi.StringOutput { return v.Description }).(pulumi.StringOutput)
}

// ID of the folder where the library panel is stored.
func (o LibraryPanelOutput) FolderId() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *LibraryPanel) pulumi.IntPtrOutput { return v.FolderId }).(pulumi.IntPtrOutput)
}

// Name of the folder containing the library panel.
func (o LibraryPanelOutput) FolderName() pulumi.StringOutput {
	return o.ApplyT(func(v *LibraryPanel) pulumi.StringOutput { return v.FolderName }).(pulumi.StringOutput)
}

// Unique ID (UID) of the folder containing the library panel.
func (o LibraryPanelOutput) FolderUid() pulumi.StringOutput {
	return o.ApplyT(func(v *LibraryPanel) pulumi.StringOutput { return v.FolderUid }).(pulumi.StringOutput)
}

// The JSON model for the library panel.
func (o LibraryPanelOutput) ModelJson() pulumi.StringOutput {
	return o.ApplyT(func(v *LibraryPanel) pulumi.StringOutput { return v.ModelJson }).(pulumi.StringOutput)
}

// Name of the library panel.
func (o LibraryPanelOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *LibraryPanel) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// The Organization ID. If not set, the Org ID defined in the provider block will be used.
func (o LibraryPanelOutput) OrgId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *LibraryPanel) pulumi.StringPtrOutput { return v.OrgId }).(pulumi.StringPtrOutput)
}

// The numeric ID of the library panel computed by Grafana.
func (o LibraryPanelOutput) PanelId() pulumi.IntOutput {
	return o.ApplyT(func(v *LibraryPanel) pulumi.IntOutput { return v.PanelId }).(pulumi.IntOutput)
}

// Type of the library panel (eg. text).
func (o LibraryPanelOutput) Type() pulumi.StringOutput {
	return o.ApplyT(func(v *LibraryPanel) pulumi.StringOutput { return v.Type }).(pulumi.StringOutput)
}

// The unique identifier (UID) of a library panel uniquely identifies library panels between multiple Grafana installs. It’s automatically generated unless you specify it during library panel creation.The UID provides consistent URLs for accessing library panels and when syncing library panels between multiple Grafana installs.
func (o LibraryPanelOutput) Uid() pulumi.StringOutput {
	return o.ApplyT(func(v *LibraryPanel) pulumi.StringOutput { return v.Uid }).(pulumi.StringOutput)
}

// Timestamp when the library panel was last modified.
func (o LibraryPanelOutput) Updated() pulumi.StringOutput {
	return o.ApplyT(func(v *LibraryPanel) pulumi.StringOutput { return v.Updated }).(pulumi.StringOutput)
}

// Version of the library panel.
func (o LibraryPanelOutput) Version() pulumi.IntOutput {
	return o.ApplyT(func(v *LibraryPanel) pulumi.IntOutput { return v.Version }).(pulumi.IntOutput)
}

type LibraryPanelArrayOutput struct{ *pulumi.OutputState }

func (LibraryPanelArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*LibraryPanel)(nil)).Elem()
}

func (o LibraryPanelArrayOutput) ToLibraryPanelArrayOutput() LibraryPanelArrayOutput {
	return o
}

func (o LibraryPanelArrayOutput) ToLibraryPanelArrayOutputWithContext(ctx context.Context) LibraryPanelArrayOutput {
	return o
}

func (o LibraryPanelArrayOutput) Index(i pulumi.IntInput) LibraryPanelOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *LibraryPanel {
		return vs[0].([]*LibraryPanel)[vs[1].(int)]
	}).(LibraryPanelOutput)
}

type LibraryPanelMapOutput struct{ *pulumi.OutputState }

func (LibraryPanelMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*LibraryPanel)(nil)).Elem()
}

func (o LibraryPanelMapOutput) ToLibraryPanelMapOutput() LibraryPanelMapOutput {
	return o
}

func (o LibraryPanelMapOutput) ToLibraryPanelMapOutputWithContext(ctx context.Context) LibraryPanelMapOutput {
	return o
}

func (o LibraryPanelMapOutput) MapIndex(k pulumi.StringInput) LibraryPanelOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *LibraryPanel {
		return vs[0].(map[string]*LibraryPanel)[vs[1].(string)]
	}).(LibraryPanelOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*LibraryPanelInput)(nil)).Elem(), &LibraryPanel{})
	pulumi.RegisterInputType(reflect.TypeOf((*LibraryPanelArrayInput)(nil)).Elem(), LibraryPanelArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*LibraryPanelMapInput)(nil)).Elem(), LibraryPanelMap{})
	pulumi.RegisterOutputType(LibraryPanelOutput{})
	pulumi.RegisterOutputType(LibraryPanelArrayOutput{})
	pulumi.RegisterOutputType(LibraryPanelMapOutput{})
}
