
{ pkgs ? import <nixpkgs> {} }:
  pkgs.mkShell {


    buildInputs = [
        pkgs.python311
        pkgs.python311Packages.pip
        pkgs.python311Packages.setuptools
        pkgs.python311Packages.wheel        
    ];

    # nativeBuildInputs is usually what you want 
    # -- tools you need to run
    nativeBuildInputs = with pkgs.buildPackages; [ 
      

    ];

}
