Title: ELF 格式

Each ELF file is made up of one ELF header, followed by file data. The file data can include:

- Program header table, describing zero or more segments
- Section header table, describing zero or more sections
- Data referred to by entries in the program header table or section header table

Files used to build a process image (execute a program) must have a program header table; relocatable files do not need one. 

![elf format](/img/ELF-layout.png)

## elf header(64 byte)

    #define EI_NIDENT       16

    typedef struct elf64_hdr {
      unsigned char e_ident[EI_NIDENT];     /* ELF "magic number" */
      Elf64_Half e_type;
      Elf64_Half e_machine;
      Elf64_Word e_version;
      Elf64_Addr e_entry;           /* Entry point virtual address */
      Elf64_Off e_phoff;            /* Program header table file offset */
      Elf64_Off e_shoff;            /* Section header table file offset */
      Elf64_Word e_flags;
      Elf64_Half e_ehsize;
      Elf64_Half e_phentsize;
      Elf64_Half e_phnum;
      Elf64_Half e_shentsize;
      Elf64_Half e_shnum;
      Elf64_Half e_shstrndx;
    } Elf64_Ehdr;

## section header table

## string table

String table sections hold null-terminated character sequences, commonly called strings. The object file uses these strings to represent symbol and section names.

## Symbol Table

An object file’s symbol table holds information needed to locate and relocate a program’s symbolic definitions and references. 

## program program header table

refer:

- [http://www.skyfree.org/linux/references/ELF_Format.pdf](http://www.skyfree.org/linux/references/ELF_Format.pdf)
- [https://en.wikipedia.org/wiki/Executable_and_Linkable_Format](https://en.wikipedia.org/wiki/Executable_and_Linkable_Format)



