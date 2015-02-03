
https://wiki.archlinux.org/index.php/KVM
http://www.cs.hs-rm.de/~linn/fachsem0910/hirt/KVM.pdf
http://www.linux-kvm.org/wiki/images/c/c5/2011-forum-native-linux-kvm-tool.pdf

http://virt-tools.org/learning/install-with-command-line/
http://blog.scottlowe.org/2012/08/21/working-with-kvm-guests/

There are a couple of different ways to create a KVM guest:

- Manually create the XML definition of the guest, then use virsh define <Name of XML file> to import the definition. You could, naturally, create a new XML definition based on an existing definition and just change a few parameters.

- Use a libvirt-compatible tool, like virt-install, to create the guest definition.
