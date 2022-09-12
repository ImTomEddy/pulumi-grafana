// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.grafana.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.grafana.inputs.FolderPermissionPermissionArgs;
import java.lang.String;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class FolderPermissionState extends com.pulumi.resources.ResourceArgs {

    public static final FolderPermissionState Empty = new FolderPermissionState();

    /**
     * The UID of the folder.
     * 
     */
    @Import(name="folderUid")
    private @Nullable Output<String> folderUid;

    /**
     * @return The UID of the folder.
     * 
     */
    public Optional<Output<String>> folderUid() {
        return Optional.ofNullable(this.folderUid);
    }

    /**
     * The permission items to add/update. Items that are omitted from the list will be removed.
     * 
     */
    @Import(name="permissions")
    private @Nullable Output<List<FolderPermissionPermissionArgs>> permissions;

    /**
     * @return The permission items to add/update. Items that are omitted from the list will be removed.
     * 
     */
    public Optional<Output<List<FolderPermissionPermissionArgs>>> permissions() {
        return Optional.ofNullable(this.permissions);
    }

    private FolderPermissionState() {}

    private FolderPermissionState(FolderPermissionState $) {
        this.folderUid = $.folderUid;
        this.permissions = $.permissions;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(FolderPermissionState defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private FolderPermissionState $;

        public Builder() {
            $ = new FolderPermissionState();
        }

        public Builder(FolderPermissionState defaults) {
            $ = new FolderPermissionState(Objects.requireNonNull(defaults));
        }

        /**
         * @param folderUid The UID of the folder.
         * 
         * @return builder
         * 
         */
        public Builder folderUid(@Nullable Output<String> folderUid) {
            $.folderUid = folderUid;
            return this;
        }

        /**
         * @param folderUid The UID of the folder.
         * 
         * @return builder
         * 
         */
        public Builder folderUid(String folderUid) {
            return folderUid(Output.of(folderUid));
        }

        /**
         * @param permissions The permission items to add/update. Items that are omitted from the list will be removed.
         * 
         * @return builder
         * 
         */
        public Builder permissions(@Nullable Output<List<FolderPermissionPermissionArgs>> permissions) {
            $.permissions = permissions;
            return this;
        }

        /**
         * @param permissions The permission items to add/update. Items that are omitted from the list will be removed.
         * 
         * @return builder
         * 
         */
        public Builder permissions(List<FolderPermissionPermissionArgs> permissions) {
            return permissions(Output.of(permissions));
        }

        /**
         * @param permissions The permission items to add/update. Items that are omitted from the list will be removed.
         * 
         * @return builder
         * 
         */
        public Builder permissions(FolderPermissionPermissionArgs... permissions) {
            return permissions(List.of(permissions));
        }

        public FolderPermissionState build() {
            return $;
        }
    }

}