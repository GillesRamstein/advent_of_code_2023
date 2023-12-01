{
  description = "Python and C Dev Env";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
    flake-utils.url = "github:numtide/flake-utils";
    poetry2nix = {
      url = "github:nix-community/poetry2nix";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };

  outputs = { self, nixpkgs, flake-utils, poetry2nix }:
    flake-utils.lib.eachDefaultSystem (system:
    let
      pkgs = nixpkgs.legacyPackages.${system};
      inherit (poetry2nix.lib.mkPoetry2Nix { inherit pkgs; }) mkPoetryEnv defaultPoetryOverrides;
      python = pkgs.python311;
    in
    with pkgs;
    {
      devShells.default = pkgs.mkShell {
        packages = [
          # C
          gcc13

          # Python
          (mkPoetryEnv {
            inherit python;
            projectDir = self;
            preferWheels = true;
            overrides = defaultPoetryOverrides.extend(self: super: {
              # jieba3k = super.jieba3k.overridePythonAttrs(old: {
              #   buildInputs = (old.buildInputs or [ ]) ++ [ super.setuptools ];
              # });
            });
          })
          nodePackages.pyright
          nodePackages_latest.vscode-json-languageserver
          ruff
          poetry
        ];
      };
    });
}
