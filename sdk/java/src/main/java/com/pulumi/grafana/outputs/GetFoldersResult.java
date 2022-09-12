// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.grafana.outputs;

import com.pulumi.core.annotations.CustomType;
import com.pulumi.grafana.outputs.GetFoldersFolder;
import java.lang.String;
import java.util.List;
import java.util.Objects;

@CustomType
public final class GetFoldersResult {
    /**
     * @return The Grafana instance&#39;s folders.
     * 
     */
    private List<GetFoldersFolder> folders;
    /**
     * @return The provider-assigned unique ID for this managed resource.
     * 
     */
    private String id;

    private GetFoldersResult() {}
    /**
     * @return The Grafana instance&#39;s folders.
     * 
     */
    public List<GetFoldersFolder> folders() {
        return this.folders;
    }
    /**
     * @return The provider-assigned unique ID for this managed resource.
     * 
     */
    public String id() {
        return this.id;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetFoldersResult defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private List<GetFoldersFolder> folders;
        private String id;
        public Builder() {}
        public Builder(GetFoldersResult defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.folders = defaults.folders;
    	      this.id = defaults.id;
        }

        @CustomType.Setter
        public Builder folders(List<GetFoldersFolder> folders) {
            this.folders = Objects.requireNonNull(folders);
            return this;
        }
        public Builder folders(GetFoldersFolder... folders) {
            return folders(List.of(folders));
        }
        @CustomType.Setter
        public Builder id(String id) {
            this.id = Objects.requireNonNull(id);
            return this;
        }
        public GetFoldersResult build() {
            final var o = new GetFoldersResult();
            o.folders = folders;
            o.id = id;
            return o;
        }
    }
}