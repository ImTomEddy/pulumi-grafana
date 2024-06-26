// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package grafana

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumiverse/pulumi-grafana/sdk/go/grafana/internal"
)

// Deprecated: grafana.index/getoncallaction.getOncallAction has been deprecated in favor of grafana.oncall/getaction.getAction
func GetOncallAction(ctx *pulumi.Context, args *GetOncallActionArgs, opts ...pulumi.InvokeOption) (*GetOncallActionResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv GetOncallActionResult
	err := ctx.Invoke("grafana:index/getOncallAction:getOncallAction", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getOncallAction.
type GetOncallActionArgs struct {
	Name string `pulumi:"name"`
}

// A collection of values returned by getOncallAction.
type GetOncallActionResult struct {
	// The provider-assigned unique ID for this managed resource.
	Id   string `pulumi:"id"`
	Name string `pulumi:"name"`
}

func GetOncallActionOutput(ctx *pulumi.Context, args GetOncallActionOutputArgs, opts ...pulumi.InvokeOption) GetOncallActionResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (GetOncallActionResult, error) {
			args := v.(GetOncallActionArgs)
			r, err := GetOncallAction(ctx, &args, opts...)
			var s GetOncallActionResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(GetOncallActionResultOutput)
}

// A collection of arguments for invoking getOncallAction.
type GetOncallActionOutputArgs struct {
	Name pulumi.StringInput `pulumi:"name"`
}

func (GetOncallActionOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetOncallActionArgs)(nil)).Elem()
}

// A collection of values returned by getOncallAction.
type GetOncallActionResultOutput struct{ *pulumi.OutputState }

func (GetOncallActionResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetOncallActionResult)(nil)).Elem()
}

func (o GetOncallActionResultOutput) ToGetOncallActionResultOutput() GetOncallActionResultOutput {
	return o
}

func (o GetOncallActionResultOutput) ToGetOncallActionResultOutputWithContext(ctx context.Context) GetOncallActionResultOutput {
	return o
}

// The provider-assigned unique ID for this managed resource.
func (o GetOncallActionResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetOncallActionResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o GetOncallActionResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v GetOncallActionResult) string { return v.Name }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(GetOncallActionResultOutput{})
}
