
{ pkgs ? import <nixpkgs> {} }:
  pkgs.mkShell {


    buildInputs = [
        pkgs.python311
        pkgs.python311Packages.pip
        pkgs.python311Packages.setuptools
        pkgs.python311Packages.wheel
        pkgs.python311Packages.build
        pkgs.python311Packages.twine
        pkgs.python311Packages.pytest
        pkgs.python311Packages.dateutils
        pkgs.ruff
    ];

    # nativeBuildInputs is usually what you want 
    # -- tools you need to run
    nativeBuildInputs = with pkgs.buildPackages; [ 
      

    ];

}
