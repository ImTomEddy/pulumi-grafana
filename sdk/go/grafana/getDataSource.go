// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package grafana

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumiverse/pulumi-grafana/sdk/go/grafana/internal"
)

// Deprecated: grafana.index/getdatasource.getDataSource has been deprecated in favor of grafana.oss/getdatasource.getDataSource
func LookupDataSource(ctx *pulumi.Context, args *LookupDataSourceArgs, opts ...pulumi.InvokeOption) (*LookupDataSourceResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupDataSourceResult
	err := ctx.Invoke("grafana:index/getDataSource:getDataSource", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getDataSource.
type LookupDataSourceArgs struct {
	// Deprecated: Use `uid` instead of `id`
	Id    *string `pulumi:"id"`
	Name  *string `pulumi:"name"`
	OrgId *string `pulumi:"orgId"`
	Uid   *string `pulumi:"uid"`
}

// A collection of values returned by getDataSource.
type LookupDataSourceResult struct {
	AccessMode        string `pulumi:"accessMode"`
	BasicAuthEnabled  bool   `pulumi:"basicAuthEnabled"`
	BasicAuthUsername string `pulumi:"basicAuthUsername"`
	DatabaseName      string `pulumi:"databaseName"`
	// Deprecated: Use `uid` instead of `id`
	Id              string  `pulumi:"id"`
	IsDefault       bool    `pulumi:"isDefault"`
	JsonDataEncoded string  `pulumi:"jsonDataEncoded"`
	Name            string  `pulumi:"name"`
	OrgId           *string `pulumi:"orgId"`
	Type            string  `pulumi:"type"`
	Uid             string  `pulumi:"uid"`
	Url             string  `pulumi:"url"`
	Username        string  `pulumi:"username"`
}

func LookupDataSourceOutput(ctx *pulumi.Context, args LookupDataSourceOutputArgs, opts ...pulumi.InvokeOption) LookupDataSourceResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupDataSourceResult, error) {
			args := v.(LookupDataSourceArgs)
			r, err := LookupDataSource(ctx, &args, opts...)
			var s LookupDataSourceResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupDataSourceResultOutput)
}

// A collection of arguments for invoking getDataSource.
type LookupDataSourceOutputArgs struct {
	// Deprecated: Use `uid` instead of `id`
	Id    pulumi.StringPtrInput `pulumi:"id"`
	Name  pulumi.StringPtrInput `pulumi:"name"`
	OrgId pulumi.StringPtrInput `pulumi:"orgId"`
	Uid   pulumi.StringPtrInput `pulumi:"uid"`
}

func (LookupDataSourceOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupDataSourceArgs)(nil)).Elem()
}

// A collection of values returned by getDataSource.
type LookupDataSourceResultOutput struct{ *pulumi.OutputState }

func (LookupDataSourceResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupDataSourceResult)(nil)).Elem()
}

func (o LookupDataSourceResultOutput) ToLookupDataSourceResultOutput() LookupDataSourceResultOutput {
	return o
}

func (o LookupDataSourceResultOutput) ToLookupDataSourceResultOutputWithContext(ctx context.Context) LookupDataSourceResultOutput {
	return o
}

func (o LookupDataSourceResultOutput) AccessMode() pulumi.StringOutput {
	return o.ApplyT(func(v LookupDataSourceResult) string { return v.AccessMode }).(pulumi.StringOutput)
}

func (o LookupDataSourceResultOutput) BasicAuthEnabled() pulumi.BoolOutput {
	return o.ApplyT(func(v LookupDataSourceResult) bool { return v.BasicAuthEnabled }).(pulumi.BoolOutput)
}

func (o LookupDataSourceResultOutput) BasicAuthUsername() pulumi.StringOutput {
	return o.ApplyT(func(v LookupDataSourceResult) string { return v.BasicAuthUsername }).(pulumi.StringOutput)
}

func (o LookupDataSourceResultOutput) DatabaseName() pulumi.StringOutput {
	return o.ApplyT(func(v LookupDataSourceResult) string { return v.DatabaseName }).(pulumi.StringOutput)
}

// Deprecated: Use `uid` instead of `id`
func (o LookupDataSourceResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupDataSourceResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o LookupDataSourceResultOutput) IsDefault() pulumi.BoolOutput {
	return o.ApplyT(func(v LookupDataSourceResult) bool { return v.IsDefault }).(pulumi.BoolOutput)
}

func (o LookupDataSourceResultOutput) JsonDataEncoded() pulumi.StringOutput {
	return o.ApplyT(func(v LookupDataSourceResult) string { return v.JsonDataEncoded }).(pulumi.StringOutput)
}

func (o LookupDataSourceResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v LookupDataSourceResult) string { return v.Name }).(pulumi.StringOutput)
}

func (o LookupDataSourceResultOutput) OrgId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDataSourceResult) *string { return v.OrgId }).(pulumi.StringPtrOutput)
}

func (o LookupDataSourceResultOutput) Type() pulumi.StringOutput {
	return o.ApplyT(func(v LookupDataSourceResult) string { return v.Type }).(pulumi.StringOutput)
}

func (o LookupDataSourceResultOutput) Uid() pulumi.StringOutput {
	return o.ApplyT(func(v LookupDataSourceResult) string { return v.Uid }).(pulumi.StringOutput)
}

func (o LookupDataSourceResultOutput) Url() pulumi.StringOutput {
	return o.ApplyT(func(v LookupDataSourceResult) string { return v.Url }).(pulumi.StringOutput)
}

func (o LookupDataSourceResultOutput) Username() pulumi.StringOutput {
	return o.ApplyT(func(v LookupDataSourceResult) string { return v.Username }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupDataSourceResultOutput{})
}
