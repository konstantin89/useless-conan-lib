# useless-conan-lib
POC for working with Conan package manager

## References

[Conan Lecture](https://www.youtube.com/watch?v=RDsn0TKcdPQ)

## Conan commands


``` bash
conan install . -g=cmake

conan create . kosta/stable

conan remove useless-lib/0.1@kosta/stable

conan upload

conan install

conan search
```