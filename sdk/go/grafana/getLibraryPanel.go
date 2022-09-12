// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package grafana

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Data source for retrieving a single library panel by name or uid.
func LookupLibraryPanel(ctx *pulumi.Context, args *LookupLibraryPanelArgs, opts ...pulumi.InvokeOption) (*LookupLibraryPanelResult, error) {
	opts = pkgInvokeDefaultOpts(opts)
	var rv LookupLibraryPanelResult
	err := ctx.Invoke("grafana:index/getLibraryPanel:getLibraryPanel", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getLibraryPanel.
type LookupLibraryPanelArgs struct {
	// Name of the library panel.
	Name *string `pulumi:"name"`
	// The unique identifier (UID) of the library panel.
	Uid *string `pulumi:"uid"`
}

// A collection of values returned by getLibraryPanel.
type LookupLibraryPanelResult struct {
	// Timestamp when the library panel was created.
	Created string `pulumi:"created"`
	// Numerical IDs of Grafana dashboards containing the library panel.
	DashboardIds []int `pulumi:"dashboardIds"`
	// Description of the library panel.
	Description string `pulumi:"description"`
	// ID of the folder where the library panel is stored.
	FolderId int `pulumi:"folderId"`
	// Name of the folder containing the library panel.
	FolderName string `pulumi:"folderName"`
	// Unique ID (UID) of the folder containing the library panel.
	FolderUid string `pulumi:"folderUid"`
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// The JSON model for the library panel.
	ModelJson string `pulumi:"modelJson"`
	// Name of the library panel.
	Name *string `pulumi:"name"`
	// The numeric ID of the library panel computed by Grafana.
	OrgId int `pulumi:"orgId"`
	// The numeric ID of the library panel computed by Grafana.
	PanelId int `pulumi:"panelId"`
	// Type of the library panel (eg. text).
	Type string `pulumi:"type"`
	// The unique identifier (UID) of the library panel.
	Uid *string `pulumi:"uid"`
	// Timestamp when the library panel was last modified.
	Updated string `pulumi:"updated"`
	// Version of the library panel.
	Version int `pulumi:"version"`
}

func LookupLibraryPanelOutput(ctx *pulumi.Context, args LookupLibraryPanelOutputArgs, opts ...pulumi.InvokeOption) LookupLibraryPanelResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupLibraryPanelResult, error) {
			args := v.(LookupLibraryPanelArgs)
			r, err := LookupLibraryPanel(ctx, &args, opts...)
			var s LookupLibraryPanelResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupLibraryPanelResultOutput)
}

// A collection of arguments for invoking getLibraryPanel.
type LookupLibraryPanelOutputArgs struct {
	// Name of the library panel.
	Name pulumi.StringPtrInput `pulumi:"name"`
	// The unique identifier (UID) of the library panel.
	Uid pulumi.StringPtrInput `pulumi:"uid"`
}

func (LookupLibraryPanelOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupLibraryPanelArgs)(nil)).Elem()
}

// A collection of values returned by getLibraryPanel.
type LookupLibraryPanelResultOutput struct{ *pulumi.OutputState }

func (LookupLibraryPanelResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupLibraryPanelResult)(nil)).Elem()
}

func (o LookupLibraryPanelResultOutput) ToLookupLibraryPanelResultOutput() LookupLibraryPanelResultOutput {
	return o
}

func (o LookupLibraryPanelResultOutput) ToLookupLibraryPanelResultOutputWithContext(ctx context.Context) LookupLibraryPanelResultOutput {
	return o
}

// Timestamp when the library panel was created.
func (o LookupLibraryPanelResultOutput) Created() pulumi.StringOutput {
	return o.ApplyT(func(v LookupLibraryPanelResult) string { return v.Created }).(pulumi.StringOutput)
}

// Numerical IDs of Grafana dashboards containing the library panel.
func (o LookupLibraryPanelResultOutput) DashboardIds() pulumi.IntArrayOutput {
	return o.ApplyT(func(v LookupLibraryPanelResult) []int { return v.DashboardIds }).(pulumi.IntArrayOutput)
}

// Description of the library panel.
func (o LookupLibraryPanelResultOutput) Description() pulumi.StringOutput {
	return o.ApplyT(func(v LookupLibraryPanelResult) string { return v.Description }).(pulumi.StringOutput)
}

// ID of the folder where the library panel is stored.
func (o LookupLibraryPanelResultOutput) FolderId() pulumi.IntOutput {
	return o.ApplyT(func(v LookupLibraryPanelResult) int { return v.FolderId }).(pulumi.IntOutput)
}

// Name of the folder containing the library panel.
func (o LookupLibraryPanelResultOutput) FolderName() pulumi.StringOutput {
	return o.ApplyT(func(v LookupLibraryPanelResult) string { return v.FolderName }).(pulumi.StringOutput)
}

// Unique ID (UID) of the folder containing the library panel.
func (o LookupLibraryPanelResultOutput) FolderUid() pulumi.StringOutput {
	return o.ApplyT(func(v LookupLibraryPanelResult) string { return v.FolderUid }).(pulumi.StringOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o LookupLibraryPanelResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupLibraryPanelResult) string { return v.Id }).(pulumi.StringOutput)
}

// The JSON model for the library panel.
func (o LookupLibraryPanelResultOutput) ModelJson() pulumi.StringOutput {
	return o.ApplyT(func(v LookupLibraryPanelResult) string { return v.ModelJson }).(pulumi.StringOutput)
}

// Name of the library panel.
func (o LookupLibraryPanelResultOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupLibraryPanelResult) *string { return v.Name }).(pulumi.StringPtrOutput)
}

// The numeric ID of the library panel computed by Grafana.
func (o LookupLibraryPanelResultOutput) OrgId() pulumi.IntOutput {
	return o.ApplyT(func(v LookupLibraryPanelResult) int { return v.OrgId }).(pulumi.IntOutput)
}

// The numeric ID of the library panel computed by Grafana.
func (o LookupLibraryPanelResultOutput) PanelId() pulumi.IntOutput {
	return o.ApplyT(func(v LookupLibraryPanelResult) int { return v.PanelId }).(pulumi.IntOutput)
}

// Type of the library panel (eg. text).
func (o LookupLibraryPanelResultOutput) Type() pulumi.StringOutput {
	return o.ApplyT(func(v LookupLibraryPanelResult) string { return v.Type }).(pulumi.StringOutput)
}

// The unique identifier (UID) of the library panel.
func (o LookupLibraryPanelResultOutput) Uid() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupLibraryPanelResult) *string { return v.Uid }).(pulumi.StringPtrOutput)
}

// Timestamp when the library panel was last modified.
func (o LookupLibraryPanelResultOutput) Updated() pulumi.StringOutput {
	return o.ApplyT(func(v LookupLibraryPanelResult) string { return v.Updated }).(pulumi.StringOutput)
}

// Version of the library panel.
func (o LookupLibraryPanelResultOutput) Version() pulumi.IntOutput {
	return o.ApplyT(func(v LookupLibraryPanelResult) int { return v.Version }).(pulumi.IntOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupLibraryPanelResultOutput{})
}