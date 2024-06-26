// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package grafana

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumiverse/pulumi-grafana/sdk/go/grafana/internal"
)

// Deprecated: grafana.index/getoncalluser.getOncallUser has been deprecated in favor of grafana.oncall/getuser.getUser
func GetOncallUser(ctx *pulumi.Context, args *GetOncallUserArgs, opts ...pulumi.InvokeOption) (*GetOncallUserResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv GetOncallUserResult
	err := ctx.Invoke("grafana:index/getOncallUser:getOncallUser", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getOncallUser.
type GetOncallUserArgs struct {
	Username string `pulumi:"username"`
}

// A collection of values returned by getOncallUser.
type GetOncallUserResult struct {
	Email string `pulumi:"email"`
	// The provider-assigned unique ID for this managed resource.
	Id       string `pulumi:"id"`
	Role     string `pulumi:"role"`
	Username string `pulumi:"username"`
}

func GetOncallUserOutput(ctx *pulumi.Context, args GetOncallUserOutputArgs, opts ...pulumi.InvokeOption) GetOncallUserResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (GetOncallUserResult, error) {
			args := v.(GetOncallUserArgs)
			r, err := GetOncallUser(ctx, &args, opts...)
			var s GetOncallUserResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(GetOncallUserResultOutput)
}

// A collection of arguments for invoking getOncallUser.
type GetOncallUserOutputArgs struct {
	Username pulumi.StringInput `pulumi:"username"`
}

func (GetOncallUserOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetOncallUserArgs)(nil)).Elem()
}

// A collection of values returned by getOncallUser.
type GetOncallUserResultOutput struct{ *pulumi.OutputState }

func (GetOncallUserResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetOncallUserResult)(nil)).Elem()
}

func (o GetOncallUserResultOutput) ToGetOncallUserResultOutput() GetOncallUserResultOutput {
	return o
}

func (o GetOncallUserResultOutput) ToGetOncallUserResultOutputWithContext(ctx context.Context) GetOncallUserResultOutput {
	return o
}

func (o GetOncallUserResultOutput) Email() pulumi.StringOutput {
	return o.ApplyT(func(v GetOncallUserResult) string { return v.Email }).(pulumi.StringOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o GetOncallUserResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetOncallUserResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o GetOncallUserResultOutput) Role() pulumi.StringOutput {
	return o.ApplyT(func(v GetOncallUserResult) string { return v.Role }).(pulumi.StringOutput)
}

func (o GetOncallUserResultOutput) Username() pulumi.StringOutput {
	return o.ApplyT(func(v GetOncallUserResult) string { return v.Username }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(GetOncallUserResultOutput{})
}
