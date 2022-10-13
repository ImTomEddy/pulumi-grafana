// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.grafana;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Export;
import com.pulumi.core.annotations.ResourceType;
import com.pulumi.core.internal.Codegen;
import com.pulumi.grafana.RoleAssignmentArgs;
import com.pulumi.grafana.Utilities;
import com.pulumi.grafana.inputs.RoleAssignmentState;
import java.lang.Integer;
import java.lang.String;
import java.util.List;
import java.util.Optional;
import javax.annotation.Nullable;

/**
 * **Note:** This resource is available only with Grafana Enterprise 9.2+.
 * * [Official documentation](https://grafana.com/docs/grafana/latest/administration/roles-and-permissions/access-control/)
 * * [HTTP API](https://grafana.com/docs/grafana/latest/developers/http_api/access_control/)
 * 
 */
@ResourceType(type="grafana:index/roleAssignment:RoleAssignment")
public class RoleAssignment extends com.pulumi.resources.CustomResource {
    /**
     * Grafana RBAC role UID.
     * 
     */
    @Export(name="roleUid", type=String.class, parameters={})
    private Output<String> roleUid;

    /**
     * @return Grafana RBAC role UID.
     * 
     */
    public Output<String> roleUid() {
        return this.roleUid;
    }
    /**
     * IDs of service accounts that the role should be assigned to.
     * 
     */
    @Export(name="serviceAccounts", type=List.class, parameters={Integer.class})
    private Output</* @Nullable */ List<Integer>> serviceAccounts;

    /**
     * @return IDs of service accounts that the role should be assigned to.
     * 
     */
    public Output<Optional<List<Integer>>> serviceAccounts() {
        return Codegen.optional(this.serviceAccounts);
    }
    /**
     * IDs of teams that the role should be assigned to.
     * 
     */
    @Export(name="teams", type=List.class, parameters={Integer.class})
    private Output</* @Nullable */ List<Integer>> teams;

    /**
     * @return IDs of teams that the role should be assigned to.
     * 
     */
    public Output<Optional<List<Integer>>> teams() {
        return Codegen.optional(this.teams);
    }
    /**
     * IDs of users that the role should be assigned to.
     * 
     */
    @Export(name="users", type=List.class, parameters={Integer.class})
    private Output</* @Nullable */ List<Integer>> users;

    /**
     * @return IDs of users that the role should be assigned to.
     * 
     */
    public Output<Optional<List<Integer>>> users() {
        return Codegen.optional(this.users);
    }

    /**
     *
     * @param name The _unique_ name of the resulting resource.
     */
    public RoleAssignment(String name) {
        this(name, RoleAssignmentArgs.Empty);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     */
    public RoleAssignment(String name, RoleAssignmentArgs args) {
        this(name, args, null);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param options A bag of options that control this resource's behavior.
     */
    public RoleAssignment(String name, RoleAssignmentArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("grafana:index/roleAssignment:RoleAssignment", name, args == null ? RoleAssignmentArgs.Empty : args, makeResourceOptions(options, Codegen.empty()));
    }

    private RoleAssignment(String name, Output<String> id, @Nullable RoleAssignmentState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("grafana:index/roleAssignment:RoleAssignment", name, state, makeResourceOptions(options, id));
    }

    private static com.pulumi.resources.CustomResourceOptions makeResourceOptions(@Nullable com.pulumi.resources.CustomResourceOptions options, @Nullable Output<String> id) {
        var defaultOptions = com.pulumi.resources.CustomResourceOptions.builder()
            .version(Utilities.getVersion())
            .build();
        return com.pulumi.resources.CustomResourceOptions.merge(defaultOptions, options, id);
    }

    /**
     * Get an existing Host resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state
     * @param options Optional settings to control the behavior of the CustomResource.
     */
    public static RoleAssignment get(String name, Output<String> id, @Nullable RoleAssignmentState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        return new RoleAssignment(name, id, state, options);
    }
}