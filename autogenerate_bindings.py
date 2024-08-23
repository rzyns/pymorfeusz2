from pathlib import Path
import litgen

def my_litgen_options() -> litgen.LitgenOptions:
    options = litgen.LitgenOptions()

    options.namespaces_root = ["morfeusz"]

    # options.srcmlcpp_options.functions_api_prefixes = "DLLIMPORT"
    options.srcmlcpp_options.flag_srcml_dump_positions = True
    options.srcmlcpp_options.fix_brace_init_default_value = True
    # options.srcmlcpp_options.header_filter_preprocessor_regions = True
    # options.srcmlcpp_options.header_filter_acceptable__regex = "^MORFEUSZ2_H$"
    options.srcmlcpp_options.ignored_warning_parts = ["SrcmlcppIgnoreElement"]
    # options.srcmlcpp_options.ignored_warnings = [WarningType.SrcmlcppIgnoreElement]

    options.class_override_virtual_methods_in_python__regex = "^Morfeusz|^ResultsIterator|^IdResolver"
    # options.fn_return_force_policy_reference_for_pointers__regex = r"MorfeuszException|what"
    # options.fn_return_force_policy_reference_for_references__regex = r"MorfeuszException|what"

    return options

def autogenerate() -> None:
    src_dir = Path("src/pymorfeusz2")
    litgen.write_generated_code_for_files(
        options=my_litgen_options(),
        input_cpp_header_files=[(src_dir / "morfeusz2.h").as_posix()],
        output_cpp_pydef_file=(src_dir / "pybind_Morfeusz2.cpp").as_posix(),
        output_stub_pyi_file=(src_dir / "__init__.pyi").as_posix(),
        # output_cpp_glue_code_file=(src_dir / "glue.cpp").as_posix(),
    )
    # options = my_litgen_options()
    # code = Path("/usr/include/morfeusz2.h").read_text()

    # result = litgen.generate_code(options, code)

    # Path(src_dir / "pybind_Morfeusz2.cpp").write_text(result.stub_code)
    # print("stub code", len(result.stub_code))
    # Path(src_dir / "__init__.pyi").write_text(result.pydef_code)
    # print("pydef code", len(result.pydef_code))
    # Path(src_dir / "gloo").write_text(result.glue_code)
    # print("glue code", len(result.glue_code))


if __name__ == "__main__":
    autogenerate()
