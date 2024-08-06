
{ pkgs ? import <nixpkgs> {} }:
  pkgs.mkShell {


    buildInputs = [
        pkgs.python312
        pkgs.python312Packages.pip
        pkgs.python312Packages.setuptools
        pkgs.python312Packages.wheel
        pkgs.python312Packages.build
        pkgs.python312Packages.twine
        pkgs.python312Packages.pytest
        pkgs.python312Packages.dateutils
        pkgs.python312Packages.confuse
        pkgs.ruff
    ];

    # nativeBuildInputs is usually what you want 
    # -- tools you need to run
    nativeBuildInputs = with pkgs.buildPackages; [ 
      

    ];

}
