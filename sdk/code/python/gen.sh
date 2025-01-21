#!/bin/bash

API_VERSION=$1

buf generate --include-imports buf.build/idnorm/ddx:$API_VERSION

update_module_imports() {
    local dir=$1
    local old_module=$2
    local new_module=$3

    find "$dir" -type f -name "*.py" -exec sed -i "s/import $old_module /import $new_module /" {} \; -exec sed -i "s/from $old_module import/from $new_module import/" {} \;
    find "$dir" -type f -name "*.pyi" -exec sed -i -E "s|$old_module|$new_module|g" {} \;

}

gen_inits() {
  local dir=$1

  find "$dir" -type d -exec touch {}/__init__.py \;
}

SRV_PROTO_SOURCE_DIR="idnorm_ddx/proto/ddx"

update_module_imports $SRV_PROTO_SOURCE_DIR "proto.ddx.v1" "idnorm_ddx.proto.ddx.v1"
update_module_imports $SRV_PROTO_SOURCE_DIR "validate" "idnorm_ddx.validate"
update_module_imports $SRV_PROTO_SOURCE_DIR "google.api" "idnorm_ddx.google.api"

gen_inits $SRV_PROTO_SOURCE_DIR

update_module_imports idnorm_ddx/validate "validate" "idnorm_ddx.validate"

gen_inits idnorm_ddx/validate

update_module_imports idnorm_ddx/google/api "google.api" "idnorm_ddx.google.api"

gen_inits idnorm_ddx/google/api
