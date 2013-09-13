# $Id$
#
# This file is part of musa.
# musa is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
# musa is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with musa. If not, see <http://www.gnu.org/licenses/>.
#

from __future__ import with_statement
import StringIO
from tarfile import TarInfo
from misc import tar_join_path, tar_add_file_from_string
import os
from exception import MusaException

licenses = {
	'GPL v2':           '''		    GNU GENERAL PUBLIC LICENSE
		       Version 2, June 1991

 Copyright (C) 1989, 1991 Free Software Foundation, Inc.,
 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

			    Preamble

  The licenses for most software are designed to take away your
freedom to share and change it.  By contrast, the GNU General Public
License is intended to guarantee your freedom to share and change free
software--to make sure the software is free for all its users.  This
General Public License applies to most of the Free Software
Foundation's software and to any other program whose authors commit to
using it.  (Some other Free Software Foundation software is covered by
the GNU Lesser General Public License instead.)  You can apply it to
your programs, too.

  When we speak of free software, we are referring to freedom, not
price.  Our General Public Licenses are designed to make sure that you
have the freedom to distribute copies of free software (and charge for
this service if you wish), that you receive source code or can get it
if you want it, that you can change the software or use pieces of it
in new free programs; and that you know you can do these things.

  To protect your rights, we need to make restrictions that forbid
anyone to deny you these rights or to ask you to surrender the rights.
These restrictions translate to certain responsibilities for you if you
distribute copies of the software, or if you modify it.

  For example, if you distribute copies of such a program, whether
gratis or for a fee, you must give the recipients all the rights that
you have.  You must make sure that they, too, receive or can get the
source code.  And you must show them these terms so they know their
rights.

  We protect your rights with two steps: (1) copyright the software, and
(2) offer you this license which gives you legal permission to copy,
distribute and/or modify the software.

  Also, for each author's protection and ours, we want to make certain
that everyone understands that there is no warranty for this free
software.  If the software is modified by someone else and passed on, we
want its recipients to know that what they have is not the original, so
that any problems introduced by others will not reflect on the original
authors' reputations.

  Finally, any free program is threatened constantly by software
patents.  We wish to avoid the danger that redistributors of a free
program will individually obtain patent licenses, in effect making the
program proprietary.  To prevent this, we have made it clear that any
patent must be licensed for everyone's free use or not licensed at all.

  The precise terms and conditions for copying, distribution and
modification follow.

		    GNU GENERAL PUBLIC LICENSE
   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

  0. This License applies to any program or other work which contains
a notice placed by the copyright holder saying it may be distributed
under the terms of this General Public License.  The "Program", below,
refers to any such program or work, and a "work based on the Program"
means either the Program or any derivative work under copyright law:
that is to say, a work containing the Program or a portion of it,
either verbatim or with modifications and/or translated into another
language.  (Hereinafter, translation is included without limitation in
the term "modification".)  Each licensee is addressed as "you".

Activities other than copying, distribution and modification are not
covered by this License; they are outside its scope.  The act of
running the Program is not restricted, and the output from the Program
is covered only if its contents constitute a work based on the
Program (independent of having been made by running the Program).
Whether that is true depends on what the Program does.

  1. You may copy and distribute verbatim copies of the Program's
source code as you receive it, in any medium, provided that you
conspicuously and appropriately publish on each copy an appropriate
copyright notice and disclaimer of warranty; keep intact all the
notices that refer to this License and to the absence of any warranty;
and give any other recipients of the Program a copy of this License
along with the Program.

You may charge a fee for the physical act of transferring a copy, and
you may at your option offer warranty protection in exchange for a fee.

  2. You may modify your copy or copies of the Program or any portion
of it, thus forming a work based on the Program, and copy and
distribute such modifications or work under the terms of Section 1
above, provided that you also meet all of these conditions:

    a) You must cause the modified files to carry prominent notices
    stating that you changed the files and the date of any change.

    b) You must cause any work that you distribute or publish, that in
    whole or in part contains or is derived from the Program or any
    part thereof, to be licensed as a whole at no charge to all third
    parties under the terms of this License.

    c) If the modified program normally reads commands interactively
    when run, you must cause it, when started running for such
    interactive use in the most ordinary way, to print or display an
    announcement including an appropriate copyright notice and a
    notice that there is no warranty (or else, saying that you provide
    a warranty) and that users may redistribute the program under
    these conditions, and telling the user how to view a copy of this
    License.  (Exception: if the Program itself is interactive but
    does not normally print such an announcement, your work based on
    the Program is not required to print an announcement.)

These requirements apply to the modified work as a whole.  If
identifiable sections of that work are not derived from the Program,
and can be reasonably considered independent and separate works in
themselves, then this License, and its terms, do not apply to those
sections when you distribute them as separate works.  But when you
distribute the same sections as part of a whole which is a work based
on the Program, the distribution of the whole must be on the terms of
this License, whose permissions for other licensees extend to the
entire whole, and thus to each and every part regardless of who wrote it.

Thus, it is not the intent of this section to claim rights or contest
your rights to work written entirely by you; rather, the intent is to
exercise the right to control the distribution of derivative or
collective works based on the Program.

In addition, mere aggregation of another work not based on the Program
with the Program (or with a work based on the Program) on a volume of
a storage or distribution medium does not bring the other work under
the scope of this License.

  3. You may copy and distribute the Program (or a work based on it,
under Section 2) in object code or executable form under the terms of
Sections 1 and 2 above provided that you also do one of the following:

    a) Accompany it with the complete corresponding machine-readable
    source code, which must be distributed under the terms of Sections
    1 and 2 above on a medium customarily used for software interchange; or,

    b) Accompany it with a written offer, valid for at least three
    years, to give any third party, for a charge no more than your
    cost of physically performing source distribution, a complete
    machine-readable copy of the corresponding source code, to be
    distributed under the terms of Sections 1 and 2 above on a medium
    customarily used for software interchange; or,

    c) Accompany it with the information you received as to the offer
    to distribute corresponding source code.  (This alternative is
    allowed only for noncommercial distribution and only if you
    received the program in object code or executable form with such
    an offer, in accord with Subsection b above.)

The source code for a work means the preferred form of the work for
making modifications to it.  For an executable work, complete source
code means all the source code for all modules it contains, plus any
associated interface definition files, plus the scripts used to
control compilation and installation of the executable.  However, as a
special exception, the source code distributed need not include
anything that is normally distributed (in either source or binary
form) with the major components (compiler, kernel, and so on) of the
operating system on which the executable runs, unless that component
itself accompanies the executable.

If distribution of executable or object code is made by offering
access to copy from a designated place, then offering equivalent
access to copy the source code from the same place counts as
distribution of the source code, even though third parties are not
compelled to copy the source along with the object code.

  4. You may not copy, modify, sublicense, or distribute the Program
except as expressly provided under this License.  Any attempt
otherwise to copy, modify, sublicense or distribute the Program is
void, and will automatically terminate your rights under this License.
However, parties who have received copies, or rights, from you under
this License will not have their licenses terminated so long as such
parties remain in full compliance.

  5. You are not required to accept this License, since you have not
signed it.  However, nothing else grants you permission to modify or
distribute the Program or its derivative works.  These actions are
prohibited by law if you do not accept this License.  Therefore, by
modifying or distributing the Program (or any work based on the
Program), you indicate your acceptance of this License to do so, and
all its terms and conditions for copying, distributing or modifying
the Program or works based on it.

  6. Each time you redistribute the Program (or any work based on the
Program), the recipient automatically receives a license from the
original licensor to copy, distribute or modify the Program subject to
these terms and conditions.  You may not impose any further
restrictions on the recipients' exercise of the rights granted herein.
You are not responsible for enforcing compliance by third parties to
this License.

  7. If, as a consequence of a court judgment or allegation of patent
infringement or for any other reason (not limited to patent issues),
conditions are imposed on you (whether by court order, agreement or
otherwise) that contradict the conditions of this License, they do not
excuse you from the conditions of this License.  If you cannot
distribute so as to satisfy simultaneously your obligations under this
License and any other pertinent obligations, then as a consequence you
may not distribute the Program at all.  For example, if a patent
license would not permit royalty-free redistribution of the Program by
all those who receive copies directly or indirectly through you, then
the only way you could satisfy both it and this License would be to
refrain entirely from distribution of the Program.

If any portion of this section is held invalid or unenforceable under
any particular circumstance, the balance of the section is intended to
apply and the section as a whole is intended to apply in other
circumstances.

It is not the purpose of this section to induce you to infringe any
patents or other property right claims or to contest validity of any
such claims; this section has the sole purpose of protecting the
integrity of the free software distribution system, which is
implemented by public license practices.  Many people have made
generous contributions to the wide range of software distributed
through that system in reliance on consistent application of that
system; it is up to the author/donor to decide if he or she is willing
to distribute software through any other system and a licensee cannot
impose that choice.

This section is intended to make thoroughly clear what is believed to
be a consequence of the rest of this License.

  8. If the distribution and/or use of the Program is restricted in
certain countries either by patents or by copyrighted interfaces, the
original copyright holder who places the Program under this License
may add an explicit geographical distribution limitation excluding
those countries, so that distribution is permitted only in or among
countries not thus excluded.  In such case, this License incorporates
the limitation as if written in the body of this License.

  9. The Free Software Foundation may publish revised and/or new versions
of the General Public License from time to time.  Such new versions will
be similar in spirit to the present version, but may differ in detail to
address new problems or concerns.

Each version is given a distinguishing version number.  If the Program
specifies a version number of this License which applies to it and "any
later version", you have the option of following the terms and conditions
either of that version or of any later version published by the Free
Software Foundation.  If the Program does not specify a version number of
this License, you may choose any version ever published by the Free Software
Foundation.

  10. If you wish to incorporate parts of the Program into other free
programs whose distribution conditions are different, write to the author
to ask for permission.  For software which is copyrighted by the Free
Software Foundation, write to the Free Software Foundation; we sometimes
make exceptions for this.  Our decision will be guided by the two goals
of preserving the free status of all derivatives of our free software and
of promoting the sharing and reuse of software generally.

			    NO WARRANTY

  11. BECAUSE THE PROGRAM IS LICENSED FREE OF CHARGE, THERE IS NO WARRANTY
FOR THE PROGRAM, TO THE EXTENT PERMITTED BY APPLICABLE LAW.  EXCEPT WHEN
OTHERWISE STATED IN WRITING THE COPYRIGHT HOLDERS AND/OR OTHER PARTIES
PROVIDE THE PROGRAM "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED
OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.  THE ENTIRE RISK AS
TO THE QUALITY AND PERFORMANCE OF THE PROGRAM IS WITH YOU.  SHOULD THE
PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF ALL NECESSARY SERVICING,
REPAIR OR CORRECTION.

  12. IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING
WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MAY MODIFY AND/OR
REDISTRIBUTE THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES,
INCLUDING ANY GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING
OUT OF THE USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED
TO LOSS OF DATA OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED BY
YOU OR THIRD PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE WITH ANY OTHER
PROGRAMS), EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE
POSSIBILITY OF SUCH DAMAGES.

		     END OF TERMS AND CONDITIONS

	    How to Apply These Terms to Your New Programs

  If you develop a new program, and you want it to be of the greatest
possible use to the public, the best way to achieve this is to make it
free software which everyone can redistribute and change under these terms.

  To do so, attach the following notices to the program.  It is safest
to attach them to the start of each source file to most effectively
convey the exclusion of warranty; and each file should have at least
the "copyright" line and a pointer to where the full notice is found.

    <one line to give the program's name and a brief idea of what it does.>
    Copyright (C) <year>  <name of author>

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with this program; if not, write to the Free Software Foundation, Inc.,
    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

Also add information on how to contact you by electronic and paper mail.

If the program is interactive, make it output a short notice like this
when it starts in an interactive mode:

    Gnomovision version 69, Copyright (C) year name of author
    Gnomovision comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
    This is free software, and you are welcome to redistribute it
    under certain conditions; type `show c' for details.

The hypothetical commands `show w' and `show c' should show the appropriate
parts of the General Public License.  Of course, the commands you use may
be called something other than `show w' and `show c'; they could even be
mouse-clicks or menu items--whatever suits your program.

You should also get your employer (if you work as a programmer) or your
school, if any, to sign a "copyright disclaimer" for the program, if
necessary.  Here is a sample; alter the names:

  Yoyodyne, Inc., hereby disclaims all copyright interest in the program
  `Gnomovision' (which makes passes at compilers) written by James Hacker.

  <signature of Ty Coon>, 1 April 1989
  Ty Coon, President of Vice

This General Public License does not permit incorporating your program into
proprietary programs.  If your program is a subroutine library, you may
consider it more useful to permit linking proprietary applications with the
library.  If this is what you want to do, use the GNU Lesser General
Public License instead of this License.
''',
	'GPL v3':           '''                    GNU GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <http://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

                            Preamble

  The GNU General Public License is a free, copyleft license for
software and other kinds of works.

  The licenses for most software and other practical works are designed
to take away your freedom to share and change the works.  By contrast,
the GNU General Public License is intended to guarantee your freedom to
share and change all versions of a program--to make sure it remains free
software for all its users.  We, the Free Software Foundation, use the
GNU General Public License for most of our software; it applies also to
any other work released this way by its authors.  You can apply it to
your programs, too.

  When we speak of free software, we are referring to freedom, not
price.  Our General Public Licenses are designed to make sure that you
have the freedom to distribute copies of free software (and charge for
them if you wish), that you receive source code or can get it if you
want it, that you can change the software or use pieces of it in new
free programs, and that you know you can do these things.

  To protect your rights, we need to prevent others from denying you
these rights or asking you to surrender the rights.  Therefore, you have
certain responsibilities if you distribute copies of the software, or if
you modify it: responsibilities to respect the freedom of others.

  For example, if you distribute copies of such a program, whether
gratis or for a fee, you must pass on to the recipients the same
freedoms that you received.  You must make sure that they, too, receive
or can get the source code.  And you must show them these terms so they
know their rights.

  Developers that use the GNU GPL protect your rights with two steps:
(1) assert copyright on the software, and (2) offer you this License
giving you legal permission to copy, distribute and/or modify it.

  For the developers' and authors' protection, the GPL clearly explains
that there is no warranty for this free software.  For both users' and
authors' sake, the GPL requires that modified versions be marked as
changed, so that their problems will not be attributed erroneously to
authors of previous versions.

  Some devices are designed to deny users access to install or run
modified versions of the software inside them, although the manufacturer
can do so.  This is fundamentally incompatible with the aim of
protecting users' freedom to change the software.  The systematic
pattern of such abuse occurs in the area of products for individuals to
use, which is precisely where it is most unacceptable.  Therefore, we
have designed this version of the GPL to prohibit the practice for those
products.  If such problems arise substantially in other domains, we
stand ready to extend this provision to those domains in future versions
of the GPL, as needed to protect the freedom of users.

  Finally, every program is threatened constantly by software patents.
States should not allow patents to restrict development and use of
software on general-purpose computers, but in those that do, we wish to
avoid the special danger that patents applied to a free program could
make it effectively proprietary.  To prevent this, the GPL assures that
patents cannot be used to render the program non-free.

  The precise terms and conditions for copying, distribution and
modification follow.

                       TERMS AND CONDITIONS

  0. Definitions.

  "This License" refers to version 3 of the GNU General Public License.

  "Copyright" also means copyright-like laws that apply to other kinds of
works, such as semiconductor masks.

  "The Program" refers to any copyrightable work licensed under this
License.  Each licensee is addressed as "you".  "Licensees" and
"recipients" may be individuals or organizations.

  To "modify" a work means to copy from or adapt all or part of the work
in a fashion requiring copyright permission, other than the making of an
exact copy.  The resulting work is called a "modified version" of the
earlier work or a work "based on" the earlier work.

  A "covered work" means either the unmodified Program or a work based
on the Program.

  To "propagate" a work means to do anything with it that, without
permission, would make you directly or secondarily liable for
infringement under applicable copyright law, except executing it on a
computer or modifying a private copy.  Propagation includes copying,
distribution (with or without modification), making available to the
public, and in some countries other activities as well.

  To "convey" a work means any kind of propagation that enables other
parties to make or receive copies.  Mere interaction with a user through
a computer network, with no transfer of a copy, is not conveying.

  An interactive user interface displays "Appropriate Legal Notices"
to the extent that it includes a convenient and prominently visible
feature that (1) displays an appropriate copyright notice, and (2)
tells the user that there is no warranty for the work (except to the
extent that warranties are provided), that licensees may convey the
work under this License, and how to view a copy of this License.  If
the interface presents a list of user commands or options, such as a
menu, a prominent item in the list meets this criterion.

  1. Source Code.

  The "source code" for a work means the preferred form of the work
for making modifications to it.  "Object code" means any non-source
form of a work.

  A "Standard Interface" means an interface that either is an official
standard defined by a recognized standards body, or, in the case of
interfaces specified for a particular programming language, one that
is widely used among developers working in that language.

  The "System Libraries" of an executable work include anything, other
than the work as a whole, that (a) is included in the normal form of
packaging a Major Component, but which is not part of that Major
Component, and (b) serves only to enable use of the work with that
Major Component, or to implement a Standard Interface for which an
implementation is available to the public in source code form.  A
"Major Component", in this context, means a major essential component
(kernel, window system, and so on) of the specific operating system
(if any) on which the executable work runs, or a compiler used to
produce the work, or an object code interpreter used to run it.

  The "Corresponding Source" for a work in object code form means all
the source code needed to generate, install, and (for an executable
work) run the object code and to modify the work, including scripts to
control those activities.  However, it does not include the work's
System Libraries, or general-purpose tools or generally available free
programs which are used unmodified in performing those activities but
which are not part of the work.  For example, Corresponding Source
includes interface definition files associated with source files for
the work, and the source code for shared libraries and dynamically
linked subprograms that the work is specifically designed to require,
such as by intimate data communication or control flow between those
subprograms and other parts of the work.

  The Corresponding Source need not include anything that users
can regenerate automatically from other parts of the Corresponding
Source.

  The Corresponding Source for a work in source code form is that
same work.

  2. Basic Permissions.

  All rights granted under this License are granted for the term of
copyright on the Program, and are irrevocable provided the stated
conditions are met.  This License explicitly affirms your unlimited
permission to run the unmodified Program.  The output from running a
covered work is covered by this License only if the output, given its
content, constitutes a covered work.  This License acknowledges your
rights of fair use or other equivalent, as provided by copyright law.

  You may make, run and propagate covered works that you do not
convey, without conditions so long as your license otherwise remains
in force.  You may convey covered works to others for the sole purpose
of having them make modifications exclusively for you, or provide you
with facilities for running those works, provided that you comply with
the terms of this License in conveying all material for which you do
not control copyright.  Those thus making or running the covered works
for you must do so exclusively on your behalf, under your direction
and control, on terms that prohibit them from making any copies of
your copyrighted material outside their relationship with you.

  Conveying under any other circumstances is permitted solely under
the conditions stated below.  Sublicensing is not allowed; section 10
makes it unnecessary.

  3. Protecting Users' Legal Rights From Anti-Circumvention Law.

  No covered work shall be deemed part of an effective technological
measure under any applicable law fulfilling obligations under article
11 of the WIPO copyright treaty adopted on 20 December 1996, or
similar laws prohibiting or restricting circumvention of such
measures.

  When you convey a covered work, you waive any legal power to forbid
circumvention of technological measures to the extent such circumvention
is effected by exercising rights under this License with respect to
the covered work, and you disclaim any intention to limit operation or
modification of the work as a means of enforcing, against the work's
users, your or third parties' legal rights to forbid circumvention of
technological measures.

  4. Conveying Verbatim Copies.

  You may convey verbatim copies of the Program's source code as you
receive it, in any medium, provided that you conspicuously and
appropriately publish on each copy an appropriate copyright notice;
keep intact all notices stating that this License and any
non-permissive terms added in accord with section 7 apply to the code;
keep intact all notices of the absence of any warranty; and give all
recipients a copy of this License along with the Program.

  You may charge any price or no price for each copy that you convey,
and you may offer support or warranty protection for a fee.

  5. Conveying Modified Source Versions.

  You may convey a work based on the Program, or the modifications to
produce it from the Program, in the form of source code under the
terms of section 4, provided that you also meet all of these conditions:

    a) The work must carry prominent notices stating that you modified
    it, and giving a relevant date.

    b) The work must carry prominent notices stating that it is
    released under this License and any conditions added under section
    7.  This requirement modifies the requirement in section 4 to
    "keep intact all notices".

    c) You must license the entire work, as a whole, under this
    License to anyone who comes into possession of a copy.  This
    License will therefore apply, along with any applicable section 7
    additional terms, to the whole of the work, and all its parts,
    regardless of how they are packaged.  This License gives no
    permission to license the work in any other way, but it does not
    invalidate such permission if you have separately received it.

    d) If the work has interactive user interfaces, each must display
    Appropriate Legal Notices; however, if the Program has interactive
    interfaces that do not display Appropriate Legal Notices, your
    work need not make them do so.

  A compilation of a covered work with other separate and independent
works, which are not by their nature extensions of the covered work,
and which are not combined with it such as to form a larger program,
in or on a volume of a storage or distribution medium, is called an
"aggregate" if the compilation and its resulting copyright are not
used to limit the access or legal rights of the compilation's users
beyond what the individual works permit.  Inclusion of a covered work
in an aggregate does not cause this License to apply to the other
parts of the aggregate.

  6. Conveying Non-Source Forms.

  You may convey a covered work in object code form under the terms
of sections 4 and 5, provided that you also convey the
machine-readable Corresponding Source under the terms of this License,
in one of these ways:

    a) Convey the object code in, or embodied in, a physical product
    (including a physical distribution medium), accompanied by the
    Corresponding Source fixed on a durable physical medium
    customarily used for software interchange.

    b) Convey the object code in, or embodied in, a physical product
    (including a physical distribution medium), accompanied by a
    written offer, valid for at least three years and valid for as
    long as you offer spare parts or customer support for that product
    model, to give anyone who possesses the object code either (1) a
    copy of the Corresponding Source for all the software in the
    product that is covered by this License, on a durable physical
    medium customarily used for software interchange, for a price no
    more than your reasonable cost of physically performing this
    conveying of source, or (2) access to copy the
    Corresponding Source from a network server at no charge.

    c) Convey individual copies of the object code with a copy of the
    written offer to provide the Corresponding Source.  This
    alternative is allowed only occasionally and noncommercially, and
    only if you received the object code with such an offer, in accord
    with subsection 6b.

    d) Convey the object code by offering access from a designated
    place (gratis or for a charge), and offer equivalent access to the
    Corresponding Source in the same way through the same place at no
    further charge.  You need not require recipients to copy the
    Corresponding Source along with the object code.  If the place to
    copy the object code is a network server, the Corresponding Source
    may be on a different server (operated by you or a third party)
    that supports equivalent copying facilities, provided you maintain
    clear directions next to the object code saying where to find the
    Corresponding Source.  Regardless of what server hosts the
    Corresponding Source, you remain obligated to ensure that it is
    available for as long as needed to satisfy these requirements.

    e) Convey the object code using peer-to-peer transmission, provided
    you inform other peers where the object code and Corresponding
    Source of the work are being offered to the general public at no
    charge under subsection 6d.

  A separable portion of the object code, whose source code is excluded
from the Corresponding Source as a System Library, need not be
included in conveying the object code work.

  A "User Product" is either (1) a "consumer product", which means any
tangible personal property which is normally used for personal, family,
or household purposes, or (2) anything designed or sold for incorporation
into a dwelling.  In determining whether a product is a consumer product,
doubtful cases shall be resolved in favor of coverage.  For a particular
product received by a particular user, "normally used" refers to a
typical or common use of that class of product, regardless of the status
of the particular user or of the way in which the particular user
actually uses, or expects or is expected to use, the product.  A product
is a consumer product regardless of whether the product has substantial
commercial, industrial or non-consumer uses, unless such uses represent
the only significant mode of use of the product.

  "Installation Information" for a User Product means any methods,
procedures, authorization keys, or other information required to install
and execute modified versions of a covered work in that User Product from
a modified version of its Corresponding Source.  The information must
suffice to ensure that the continued functioning of the modified object
code is in no case prevented or interfered with solely because
modification has been made.

  If you convey an object code work under this section in, or with, or
specifically for use in, a User Product, and the conveying occurs as
part of a transaction in which the right of possession and use of the
User Product is transferred to the recipient in perpetuity or for a
fixed term (regardless of how the transaction is characterized), the
Corresponding Source conveyed under this section must be accompanied
by the Installation Information.  But this requirement does not apply
if neither you nor any third party retains the ability to install
modified object code on the User Product (for example, the work has
been installed in ROM).

  The requirement to provide Installation Information does not include a
requirement to continue to provide support service, warranty, or updates
for a work that has been modified or installed by the recipient, or for
the User Product in which it has been modified or installed.  Access to a
network may be denied when the modification itself materially and
adversely affects the operation of the network or violates the rules and
protocols for communication across the network.

  Corresponding Source conveyed, and Installation Information provided,
in accord with this section must be in a format that is publicly
documented (and with an implementation available to the public in
source code form), and must require no special password or key for
unpacking, reading or copying.

  7. Additional Terms.

  "Additional permissions" are terms that supplement the terms of this
License by making exceptions from one or more of its conditions.
Additional permissions that are applicable to the entire Program shall
be treated as though they were included in this License, to the extent
that they are valid under applicable law.  If additional permissions
apply only to part of the Program, that part may be used separately
under those permissions, but the entire Program remains governed by
this License without regard to the additional permissions.

  When you convey a copy of a covered work, you may at your option
remove any additional permissions from that copy, or from any part of
it.  (Additional permissions may be written to require their own
removal in certain cases when you modify the work.)  You may place
additional permissions on material, added by you to a covered work,
for which you have or can give appropriate copyright permission.

  Notwithstanding any other provision of this License, for material you
add to a covered work, you may (if authorized by the copyright holders of
that material) supplement the terms of this License with terms:

    a) Disclaiming warranty or limiting liability differently from the
    terms of sections 15 and 16 of this License; or

    b) Requiring preservation of specified reasonable legal notices or
    author attributions in that material or in the Appropriate Legal
    Notices displayed by works containing it; or

    c) Prohibiting misrepresentation of the origin of that material, or
    requiring that modified versions of such material be marked in
    reasonable ways as different from the original version; or

    d) Limiting the use for publicity purposes of names of licensors or
    authors of the material; or

    e) Declining to grant rights under trademark law for use of some
    trade names, trademarks, or service marks; or

    f) Requiring indemnification of licensors and authors of that
    material by anyone who conveys the material (or modified versions of
    it) with contractual assumptions of liability to the recipient, for
    any liability that these contractual assumptions directly impose on
    those licensors and authors.

  All other non-permissive additional terms are considered "further
restrictions" within the meaning of section 10.  If the Program as you
received it, or any part of it, contains a notice stating that it is
governed by this License along with a term that is a further
restriction, you may remove that term.  If a license document contains
a further restriction but permits relicensing or conveying under this
License, you may add to a covered work material governed by the terms
of that license document, provided that the further restriction does
not survive such relicensing or conveying.

  If you add terms to a covered work in accord with this section, you
must place, in the relevant source files, a statement of the
additional terms that apply to those files, or a notice indicating
where to find the applicable terms.

  Additional terms, permissive or non-permissive, may be stated in the
form of a separately written license, or stated as exceptions;
the above requirements apply either way.

  8. Termination.

  You may not propagate or modify a covered work except as expressly
provided under this License.  Any attempt otherwise to propagate or
modify it is void, and will automatically terminate your rights under
this License (including any patent licenses granted under the third
paragraph of section 11).

  However, if you cease all violation of this License, then your
license from a particular copyright holder is reinstated (a)
provisionally, unless and until the copyright holder explicitly and
finally terminates your license, and (b) permanently, if the copyright
holder fails to notify you of the violation by some reasonable means
prior to 60 days after the cessation.

  Moreover, your license from a particular copyright holder is
reinstated permanently if the copyright holder notifies you of the
violation by some reasonable means, this is the first time you have
received notice of violation of this License (for any work) from that
copyright holder, and you cure the violation prior to 30 days after
your receipt of the notice.

  Termination of your rights under this section does not terminate the
licenses of parties who have received copies or rights from you under
this License.  If your rights have been terminated and not permanently
reinstated, you do not qualify to receive new licenses for the same
material under section 10.

  9. Acceptance Not Required for Having Copies.

  You are not required to accept this License in order to receive or
run a copy of the Program.  Ancillary propagation of a covered work
occurring solely as a consequence of using peer-to-peer transmission
to receive a copy likewise does not require acceptance.  However,
nothing other than this License grants you permission to propagate or
modify any covered work.  These actions infringe copyright if you do
not accept this License.  Therefore, by modifying or propagating a
covered work, you indicate your acceptance of this License to do so.

  10. Automatic Licensing of Downstream Recipients.

  Each time you convey a covered work, the recipient automatically
receives a license from the original licensors, to run, modify and
propagate that work, subject to this License.  You are not responsible
for enforcing compliance by third parties with this License.

  An "entity transaction" is a transaction transferring control of an
organization, or substantially all assets of one, or subdividing an
organization, or merging organizations.  If propagation of a covered
work results from an entity transaction, each party to that
transaction who receives a copy of the work also receives whatever
licenses to the work the party's predecessor in interest had or could
give under the previous paragraph, plus a right to possession of the
Corresponding Source of the work from the predecessor in interest, if
the predecessor has it or can get it with reasonable efforts.

  You may not impose any further restrictions on the exercise of the
rights granted or affirmed under this License.  For example, you may
not impose a license fee, royalty, or other charge for exercise of
rights granted under this License, and you may not initiate litigation
(including a cross-claim or counterclaim in a lawsuit) alleging that
any patent claim is infringed by making, using, selling, offering for
sale, or importing the Program or any portion of it.

  11. Patents.

  A "contributor" is a copyright holder who authorizes use under this
License of the Program or a work on which the Program is based.  The
work thus licensed is called the contributor's "contributor version".

  A contributor's "essential patent claims" are all patent claims
owned or controlled by the contributor, whether already acquired or
hereafter acquired, that would be infringed by some manner, permitted
by this License, of making, using, or selling its contributor version,
but do not include claims that would be infringed only as a
consequence of further modification of the contributor version.  For
purposes of this definition, "control" includes the right to grant
patent sublicenses in a manner consistent with the requirements of
this License.

  Each contributor grants you a non-exclusive, worldwide, royalty-free
patent license under the contributor's essential patent claims, to
make, use, sell, offer for sale, import and otherwise run, modify and
propagate the contents of its contributor version.

  In the following three paragraphs, a "patent license" is any express
agreement or commitment, however denominated, not to enforce a patent
(such as an express permission to practice a patent or covenant not to
sue for patent infringement).  To "grant" such a patent license to a
party means to make such an agreement or commitment not to enforce a
patent against the party.

  If you convey a covered work, knowingly relying on a patent license,
and the Corresponding Source of the work is not available for anyone
to copy, free of charge and under the terms of this License, through a
publicly available network server or other readily accessible means,
then you must either (1) cause the Corresponding Source to be so
available, or (2) arrange to deprive yourself of the benefit of the
patent license for this particular work, or (3) arrange, in a manner
consistent with the requirements of this License, to extend the patent
license to downstream recipients.  "Knowingly relying" means you have
actual knowledge that, but for the patent license, your conveying the
covered work in a country, or your recipient's use of the covered work
in a country, would infringe one or more identifiable patents in that
country that you have reason to believe are valid.

  If, pursuant to or in connection with a single transaction or
arrangement, you convey, or propagate by procuring conveyance of, a
covered work, and grant a patent license to some of the parties
receiving the covered work authorizing them to use, propagate, modify
or convey a specific copy of the covered work, then the patent license
you grant is automatically extended to all recipients of the covered
work and works based on it.

  A patent license is "discriminatory" if it does not include within
the scope of its coverage, prohibits the exercise of, or is
conditioned on the non-exercise of one or more of the rights that are
specifically granted under this License.  You may not convey a covered
work if you are a party to an arrangement with a third party that is
in the business of distributing software, under which you make payment
to the third party based on the extent of your activity of conveying
the work, and under which the third party grants, to any of the
parties who would receive the covered work from you, a discriminatory
patent license (a) in connection with copies of the covered work
conveyed by you (or copies made from those copies), or (b) primarily
for and in connection with specific products or compilations that
contain the covered work, unless you entered into that arrangement,
or that patent license was granted, prior to 28 March 2007.

  Nothing in this License shall be construed as excluding or limiting
any implied license or other defenses to infringement that may
otherwise be available to you under applicable patent law.

  12. No Surrender of Others' Freedom.

  If conditions are imposed on you (whether by court order, agreement or
otherwise) that contradict the conditions of this License, they do not
excuse you from the conditions of this License.  If you cannot convey a
covered work so as to satisfy simultaneously your obligations under this
License and any other pertinent obligations, then as a consequence you may
not convey it at all.  For example, if you agree to terms that obligate you
to collect a royalty for further conveying from those to whom you convey
the Program, the only way you could satisfy both those terms and this
License would be to refrain entirely from conveying the Program.

  13. Use with the GNU Affero General Public License.

  Notwithstanding any other provision of this License, you have
permission to link or combine any covered work with a work licensed
under version 3 of the GNU Affero General Public License into a single
combined work, and to convey the resulting work.  The terms of this
License will continue to apply to the part which is the covered work,
but the special requirements of the GNU Affero General Public License,
section 13, concerning interaction through a network will apply to the
combination as such.

  14. Revised Versions of this License.

  The Free Software Foundation may publish revised and/or new versions of
the GNU General Public License from time to time.  Such new versions will
be similar in spirit to the present version, but may differ in detail to
address new problems or concerns.

  Each version is given a distinguishing version number.  If the
Program specifies that a certain numbered version of the GNU General
Public License "or any later version" applies to it, you have the
option of following the terms and conditions either of that numbered
version or of any later version published by the Free Software
Foundation.  If the Program does not specify a version number of the
GNU General Public License, you may choose any version ever published
by the Free Software Foundation.

  If the Program specifies that a proxy can decide which future
versions of the GNU General Public License can be used, that proxy's
public statement of acceptance of a version permanently authorizes you
to choose that version for the Program.

  Later license versions may give you additional or different
permissions.  However, no additional obligations are imposed on any
author or copyright holder as a result of your choosing to follow a
later version.

  15. Disclaimer of Warranty.

  THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY
APPLICABLE LAW.  EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT
HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM "AS IS" WITHOUT WARRANTY
OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO,
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
PURPOSE.  THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM
IS WITH YOU.  SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF
ALL NECESSARY SERVICING, REPAIR OR CORRECTION.

  16. Limitation of Liability.

  IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING
WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MODIFIES AND/OR CONVEYS
THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES, INCLUDING ANY
GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE
USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED TO LOSS OF
DATA OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED BY YOU OR THIRD
PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE WITH ANY OTHER PROGRAMS),
EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF
SUCH DAMAGES.

  17. Interpretation of Sections 15 and 16.

  If the disclaimer of warranty and limitation of liability provided
above cannot be given local legal effect according to their terms,
reviewing courts shall apply local law that most closely approximates
an absolute waiver of all civil liability in connection with the
Program, unless a warranty or assumption of liability accompanies a
copy of the Program in return for a fee.

                     END OF TERMS AND CONDITIONS

            How to Apply These Terms to Your New Programs

  If you develop a new program, and you want it to be of the greatest
possible use to the public, the best way to achieve this is to make it
free software which everyone can redistribute and change under these terms.

  To do so, attach the following notices to the program.  It is safest
to attach them to the start of each source file to most effectively
state the exclusion of warranty; and each file should have at least
the "copyright" line and a pointer to where the full notice is found.

    <one line to give the program's name and a brief idea of what it does.>
    Copyright (C) <year>  <name of author>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

Also add information on how to contact you by electronic and paper mail.

  If the program does terminal interaction, make it output a short
notice like this when it starts in an interactive mode:

    <program>  Copyright (C) <year>  <name of author>
    This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
    This is free software, and you are welcome to redistribute it
    under certain conditions; type `show c' for details.

The hypothetical commands `show w' and `show c' should show the appropriate
parts of the General Public License.  Of course, your program's commands
might be different; for a GUI interface, you would use an "about box".

  You should also get your employer (if you work as a programmer) or school,
if any, to sign a "copyright disclaimer" for the program, if necessary.
For more information on this, and how to apply and follow the GNU GPL, see
<http://www.gnu.org/licenses/>.

  The GNU General Public License does not permit incorporating your program
into proprietary programs.  If your program is a subroutine library, you
may consider it more useful to permit linking proprietary applications with
the library.  If this is what you want to do, use the GNU Lesser General
Public License instead of this License.  But first, please read
<http://www.gnu.org/philosophy/why-not-lgpl.html>.
''',
	'LGPL v2.1':        '''                  GNU LESSER GENERAL PUBLIC LICENSE
                       Version 2.1, February 1999

 Copyright (C) 1991, 1999 Free Software Foundation, Inc.
 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

[This is the first released version of the Lesser GPL.  It also counts
 as the successor of the GNU Library Public License, version 2, hence
 the version number 2.1.]

                            Preamble

  The licenses for most software are designed to take away your
freedom to share and change it.  By contrast, the GNU General Public
Licenses are intended to guarantee your freedom to share and change
free software--to make sure the software is free for all its users.

  This license, the Lesser General Public License, applies to some
specially designated software packages--typically libraries--of the
Free Software Foundation and other authors who decide to use it.  You
can use it too, but we suggest you first think carefully about whether
this license or the ordinary General Public License is the better
strategy to use in any particular case, based on the explanations below.

  When we speak of free software, we are referring to freedom of use,
not price.  Our General Public Licenses are designed to make sure that
you have the freedom to distribute copies of free software (and charge
for this service if you wish); that you receive source code or can get
it if you want it; that you can change the software and use pieces of
it in new free programs; and that you are informed that you can do
these things.

  To protect your rights, we need to make restrictions that forbid
distributors to deny you these rights or to ask you to surrender these
rights.  These restrictions translate to certain responsibilities for
you if you distribute copies of the library or if you modify it.

  For example, if you distribute copies of the library, whether gratis
or for a fee, you must give the recipients all the rights that we gave
you.  You must make sure that they, too, receive or can get the source
code.  If you link other code with the library, you must provide
complete object files to the recipients, so that they can relink them
with the library after making changes to the library and recompiling
it.  And you must show them these terms so they know their rights.

  We protect your rights with a two-step method: (1) we copyright the
library, and (2) we offer you this license, which gives you legal
permission to copy, distribute and/or modify the library.

  To protect each distributor, we want to make it very clear that
there is no warranty for the free library.  Also, if the library is
modified by someone else and passed on, the recipients should know
that what they have is not the original version, so that the original
author's reputation will not be affected by problems that might be
introduced by others.

  Finally, software patents pose a constant threat to the existence of
any free program.  We wish to make sure that a company cannot
effectively restrict the users of a free program by obtaining a
restrictive license from a patent holder.  Therefore, we insist that
any patent license obtained for a version of the library must be
consistent with the full freedom of use specified in this license.

  Most GNU software, including some libraries, is covered by the
ordinary GNU General Public License.  This license, the GNU Lesser
General Public License, applies to certain designated libraries, and
is quite different from the ordinary General Public License.  We use
this license for certain libraries in order to permit linking those
libraries into non-free programs.

  When a program is linked with a library, whether statically or using
a shared library, the combination of the two is legally speaking a
combined work, a derivative of the original library.  The ordinary
General Public License therefore permits such linking only if the
entire combination fits its criteria of freedom.  The Lesser General
Public License permits more lax criteria for linking other code with
the library.

  We call this license the "Lesser" General Public License because it
does Less to protect the user's freedom than the ordinary General
Public License.  It also provides other free software developers Less
of an advantage over competing non-free programs.  These disadvantages
are the reason we use the ordinary General Public License for many
libraries.  However, the Lesser license provides advantages in certain
special circumstances.

  For example, on rare occasions, there may be a special need to
encourage the widest possible use of a certain library, so that it becomes
a de-facto standard.  To achieve this, non-free programs must be
allowed to use the library.  A more frequent case is that a free
library does the same job as widely used non-free libraries.  In this
case, there is little to gain by limiting the free library to free
software only, so we use the Lesser General Public License.

  In other cases, permission to use a particular library in non-free
programs enables a greater number of people to use a large body of
free software.  For example, permission to use the GNU C Library in
non-free programs enables many more people to use the whole GNU
operating system, as well as its variant, the GNU/Linux operating
system.

  Although the Lesser General Public License is Less protective of the
users' freedom, it does ensure that the user of a program that is
linked with the Library has the freedom and the wherewithal to run
that program using a modified version of the Library.

  The precise terms and conditions for copying, distribution and
modification follow.  Pay close attention to the difference between a
"work based on the library" and a "work that uses the library".  The
former contains code derived from the library, whereas the latter must
be combined with the library in order to run.

                  GNU LESSER GENERAL PUBLIC LICENSE
   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

  0. This License Agreement applies to any software library or other
program which contains a notice placed by the copyright holder or
other authorized party saying it may be distributed under the terms of
this Lesser General Public License (also called "this License").
Each licensee is addressed as "you".

  A "library" means a collection of software functions and/or data
prepared so as to be conveniently linked with application programs
(which use some of those functions and data) to form executables.

  The "Library", below, refers to any such software library or work
which has been distributed under these terms.  A "work based on the
Library" means either the Library or any derivative work under
copyright law: that is to say, a work containing the Library or a
portion of it, either verbatim or with modifications and/or translated
straightforwardly into another language.  (Hereinafter, translation is
included without limitation in the term "modification".)

  "Source code" for a work means the preferred form of the work for
making modifications to it.  For a library, complete source code means
all the source code for all modules it contains, plus any associated
interface definition files, plus the scripts used to control compilation
and installation of the library.

  Activities other than copying, distribution and modification are not
covered by this License; they are outside its scope.  The act of
running a program using the Library is not restricted, and output from
such a program is covered only if its contents constitute a work based
on the Library (independent of the use of the Library in a tool for
writing it).  Whether that is true depends on what the Library does
and what the program that uses the Library does.

  1. You may copy and distribute verbatim copies of the Library's
complete source code as you receive it, in any medium, provided that
you conspicuously and appropriately publish on each copy an
appropriate copyright notice and disclaimer of warranty; keep intact
all the notices that refer to this License and to the absence of any
warranty; and distribute a copy of this License along with the
Library.

  You may charge a fee for the physical act of transferring a copy,
and you may at your option offer warranty protection in exchange for a
fee.

  2. You may modify your copy or copies of the Library or any portion
of it, thus forming a work based on the Library, and copy and
distribute such modifications or work under the terms of Section 1
above, provided that you also meet all of these conditions:

    a) The modified work must itself be a software library.

    b) You must cause the files modified to carry prominent notices
    stating that you changed the files and the date of any change.

    c) You must cause the whole of the work to be licensed at no
    charge to all third parties under the terms of this License.

    d) If a facility in the modified Library refers to a function or a
    table of data to be supplied by an application program that uses
    the facility, other than as an argument passed when the facility
    is invoked, then you must make a good faith effort to ensure that,
    in the event an application does not supply such function or
    table, the facility still operates, and performs whatever part of
    its purpose remains meaningful.

    (For example, a function in a library to compute square roots has
    a purpose that is entirely well-defined independent of the
    application.  Therefore, Subsection 2d requires that any
    application-supplied function or table used by this function must
    be optional: if the application does not supply it, the square
    root function must still compute square roots.)

These requirements apply to the modified work as a whole.  If
identifiable sections of that work are not derived from the Library,
and can be reasonably considered independent and separate works in
themselves, then this License, and its terms, do not apply to those
sections when you distribute them as separate works.  But when you
distribute the same sections as part of a whole which is a work based
on the Library, the distribution of the whole must be on the terms of
this License, whose permissions for other licensees extend to the
entire whole, and thus to each and every part regardless of who wrote
it.

Thus, it is not the intent of this section to claim rights or contest
your rights to work written entirely by you; rather, the intent is to
exercise the right to control the distribution of derivative or
collective works based on the Library.

In addition, mere aggregation of another work not based on the Library
with the Library (or with a work based on the Library) on a volume of
a storage or distribution medium does not bring the other work under
the scope of this License.

  3. You may opt to apply the terms of the ordinary GNU General Public
License instead of this License to a given copy of the Library.  To do
this, you must alter all the notices that refer to this License, so
that they refer to the ordinary GNU General Public License, version 2,
instead of to this License.  (If a newer version than version 2 of the
ordinary GNU General Public License has appeared, then you can specify
that version instead if you wish.)  Do not make any other change in
these notices.

  Once this change is made in a given copy, it is irreversible for
that copy, so the ordinary GNU General Public License applies to all
subsequent copies and derivative works made from that copy.

  This option is useful when you wish to copy part of the code of
the Library into a program that is not a library.

  4. You may copy and distribute the Library (or a portion or
derivative of it, under Section 2) in object code or executable form
under the terms of Sections 1 and 2 above provided that you accompany
it with the complete corresponding machine-readable source code, which
must be distributed under the terms of Sections 1 and 2 above on a
medium customarily used for software interchange.

  If distribution of object code is made by offering access to copy
from a designated place, then offering equivalent access to copy the
source code from the same place satisfies the requirement to
distribute the source code, even though third parties are not
compelled to copy the source along with the object code.

  5. A program that contains no derivative of any portion of the
Library, but is designed to work with the Library by being compiled or
linked with it, is called a "work that uses the Library".  Such a
work, in isolation, is not a derivative work of the Library, and
therefore falls outside the scope of this License.

  However, linking a "work that uses the Library" with the Library
creates an executable that is a derivative of the Library (because it
contains portions of the Library), rather than a "work that uses the
library".  The executable is therefore covered by this License.
Section 6 states terms for distribution of such executables.

  When a "work that uses the Library" uses material from a header file
that is part of the Library, the object code for the work may be a
derivative work of the Library even though the source code is not.
Whether this is true is especially significant if the work can be
linked without the Library, or if the work is itself a library.  The
threshold for this to be true is not precisely defined by law.

  If such an object file uses only numerical parameters, data
structure layouts and accessors, and small macros and small inline
functions (ten lines or less in length), then the use of the object
file is unrestricted, regardless of whether it is legally a derivative
work.  (Executables containing this object code plus portions of the
Library will still fall under Section 6.)

  Otherwise, if the work is a derivative of the Library, you may
distribute the object code for the work under the terms of Section 6.
Any executables containing that work also fall under Section 6,
whether or not they are linked directly with the Library itself.

  6. As an exception to the Sections above, you may also combine or
link a "work that uses the Library" with the Library to produce a
work containing portions of the Library, and distribute that work
under terms of your choice, provided that the terms permit
modification of the work for the customer's own use and reverse
engineering for debugging such modifications.

  You must give prominent notice with each copy of the work that the
Library is used in it and that the Library and its use are covered by
this License.  You must supply a copy of this License.  If the work
during execution displays copyright notices, you must include the
copyright notice for the Library among them, as well as a reference
directing the user to the copy of this License.  Also, you must do one
of these things:

    a) Accompany the work with the complete corresponding
    machine-readable source code for the Library including whatever
    changes were used in the work (which must be distributed under
    Sections 1 and 2 above); and, if the work is an executable linked
    with the Library, with the complete machine-readable "work that
    uses the Library", as object code and/or source code, so that the
    user can modify the Library and then relink to produce a modified
    executable containing the modified Library.  (It is understood
    that the user who changes the contents of definitions files in the
    Library will not necessarily be able to recompile the application
    to use the modified definitions.)

    b) Use a suitable shared library mechanism for linking with the
    Library.  A suitable mechanism is one that (1) uses at run time a
    copy of the library already present on the user's computer system,
    rather than copying library functions into the executable, and (2)
    will operate properly with a modified version of the library, if
    the user installs one, as long as the modified version is
    interface-compatible with the version that the work was made with.

    c) Accompany the work with a written offer, valid for at
    least three years, to give the same user the materials
    specified in Subsection 6a, above, for a charge no more
    than the cost of performing this distribution.

    d) If distribution of the work is made by offering access to copy
    from a designated place, offer equivalent access to copy the above
    specified materials from the same place.

    e) Verify that the user has already received a copy of these
    materials or that you have already sent this user a copy.

  For an executable, the required form of the "work that uses the
Library" must include any data and utility programs needed for
reproducing the executable from it.  However, as a special exception,
the materials to be distributed need not include anything that is
normally distributed (in either source or binary form) with the major
components (compiler, kernel, and so on) of the operating system on
which the executable runs, unless that component itself accompanies
the executable.

  It may happen that this requirement contradicts the license
restrictions of other proprietary libraries that do not normally
accompany the operating system.  Such a contradiction means you cannot
use both them and the Library together in an executable that you
distribute.

  7. You may place library facilities that are a work based on the
Library side-by-side in a single library together with other library
facilities not covered by this License, and distribute such a combined
library, provided that the separate distribution of the work based on
the Library and of the other library facilities is otherwise
permitted, and provided that you do these two things:

    a) Accompany the combined library with a copy of the same work
    based on the Library, uncombined with any other library
    facilities.  This must be distributed under the terms of the
    Sections above.

    b) Give prominent notice with the combined library of the fact
    that part of it is a work based on the Library, and explaining
    where to find the accompanying uncombined form of the same work.

  8. You may not copy, modify, sublicense, link with, or distribute
the Library except as expressly provided under this License.  Any
attempt otherwise to copy, modify, sublicense, link with, or
distribute the Library is void, and will automatically terminate your
rights under this License.  However, parties who have received copies,
or rights, from you under this License will not have their licenses
terminated so long as such parties remain in full compliance.

  9. You are not required to accept this License, since you have not
signed it.  However, nothing else grants you permission to modify or
distribute the Library or its derivative works.  These actions are
prohibited by law if you do not accept this License.  Therefore, by
modifying or distributing the Library (or any work based on the
Library), you indicate your acceptance of this License to do so, and
all its terms and conditions for copying, distributing or modifying
the Library or works based on it.

  10. Each time you redistribute the Library (or any work based on the
Library), the recipient automatically receives a license from the
original licensor to copy, distribute, link with or modify the Library
subject to these terms and conditions.  You may not impose any further
restrictions on the recipients' exercise of the rights granted herein.
You are not responsible for enforcing compliance by third parties with
this License.

  11. If, as a consequence of a court judgment or allegation of patent
infringement or for any other reason (not limited to patent issues),
conditions are imposed on you (whether by court order, agreement or
otherwise) that contradict the conditions of this License, they do not
excuse you from the conditions of this License.  If you cannot
distribute so as to satisfy simultaneously your obligations under this
License and any other pertinent obligations, then as a consequence you
may not distribute the Library at all.  For example, if a patent
license would not permit royalty-free redistribution of the Library by
all those who receive copies directly or indirectly through you, then
the only way you could satisfy both it and this License would be to
refrain entirely from distribution of the Library.

If any portion of this section is held invalid or unenforceable under any
particular circumstance, the balance of the section is intended to apply,
and the section as a whole is intended to apply in other circumstances.

It is not the purpose of this section to induce you to infringe any
patents or other property right claims or to contest validity of any
such claims; this section has the sole purpose of protecting the
integrity of the free software distribution system which is
implemented by public license practices.  Many people have made
generous contributions to the wide range of software distributed
through that system in reliance on consistent application of that
system; it is up to the author/donor to decide if he or she is willing
to distribute software through any other system and a licensee cannot
impose that choice.

This section is intended to make thoroughly clear what is believed to
be a consequence of the rest of this License.

  12. If the distribution and/or use of the Library is restricted in
certain countries either by patents or by copyrighted interfaces, the
original copyright holder who places the Library under this License may add
an explicit geographical distribution limitation excluding those countries,
so that distribution is permitted only in or among countries not thus
excluded.  In such case, this License incorporates the limitation as if
written in the body of this License.

  13. The Free Software Foundation may publish revised and/or new
versions of the Lesser General Public License from time to time.
Such new versions will be similar in spirit to the present version,
but may differ in detail to address new problems or concerns.

Each version is given a distinguishing version number.  If the Library
specifies a version number of this License which applies to it and
"any later version", you have the option of following the terms and
conditions either of that version or of any later version published by
the Free Software Foundation.  If the Library does not specify a
license version number, you may choose any version ever published by
the Free Software Foundation.

  14. If you wish to incorporate parts of the Library into other free
programs whose distribution conditions are incompatible with these,
write to the author to ask for permission.  For software which is
copyrighted by the Free Software Foundation, write to the Free
Software Foundation; we sometimes make exceptions for this.  Our
decision will be guided by the two goals of preserving the free status
of all derivatives of our free software and of promoting the sharing
and reuse of software generally.

                            NO WARRANTY

  15. BECAUSE THE LIBRARY IS LICENSED FREE OF CHARGE, THERE IS NO
WARRANTY FOR THE LIBRARY, TO THE EXTENT PERMITTED BY APPLICABLE LAW.
EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT HOLDERS AND/OR
OTHER PARTIES PROVIDE THE LIBRARY "AS IS" WITHOUT WARRANTY OF ANY
KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
PURPOSE.  THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE
LIBRARY IS WITH YOU.  SHOULD THE LIBRARY PROVE DEFECTIVE, YOU ASSUME
THE COST OF ALL NECESSARY SERVICING, REPAIR OR CORRECTION.

  16. IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN
WRITING WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MAY MODIFY
AND/OR REDISTRIBUTE THE LIBRARY AS PERMITTED ABOVE, BE LIABLE TO YOU
FOR DAMAGES, INCLUDING ANY GENERAL, SPECIAL, INCIDENTAL OR
CONSEQUENTIAL DAMAGES ARISING OUT OF THE USE OR INABILITY TO USE THE
LIBRARY (INCLUDING BUT NOT LIMITED TO LOSS OF DATA OR DATA BEING
RENDERED INACCURATE OR LOSSES SUSTAINED BY YOU OR THIRD PARTIES OR A
FAILURE OF THE LIBRARY TO OPERATE WITH ANY OTHER SOFTWARE), EVEN IF
SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH
DAMAGES.

                     END OF TERMS AND CONDITIONS

           How to Apply These Terms to Your New Libraries

  If you develop a new library, and you want it to be of the greatest
possible use to the public, we recommend making it free software that
everyone can redistribute and change.  You can do so by permitting
redistribution under these terms (or, alternatively, under the terms of the
ordinary General Public License).

  To apply these terms, attach the following notices to the library.  It is
safest to attach them to the start of each source file to most effectively
convey the exclusion of warranty; and each file should have at least the
"copyright" line and a pointer to where the full notice is found.

    <one line to give the library's name and a brief idea of what it does.>
    Copyright (C) <year>  <name of author>

    This library is free software; you can redistribute it and/or
    modify it under the terms of the GNU Lesser General Public
    License as published by the Free Software Foundation; either
    version 2.1 of the License, or (at your option) any later version.

    This library is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
    Lesser General Public License for more details.

    You should have received a copy of the GNU Lesser General Public
    License along with this library; if not, write to the Free Software
    Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA

Also add information on how to contact you by electronic and paper mail.

You should also get your employer (if you work as a programmer) or your
school, if any, to sign a "copyright disclaimer" for the library, if
necessary.  Here is a sample; alter the names:

  Yoyodyne, Inc., hereby disclaims all copyright interest in the
  library `Frob' (a library for tweaking knobs) written by James Random Hacker.

  <signature of Ty Coon>, 1 April 1990
  Ty Coon, President of Vice

That's all there is to it!
''',
	'CC-0 v1.0':        '''


                               Creative Commons
****** Creative Commons Legal Code ******
***** CC0 1.0 Universal *****
     CREATIVE COMMONS CORPORATION IS NOT A LAW FIRM AND DOES NOT PROVIDE
     LEGAL SERVICES. DISTRIBUTION OF THIS DOCUMENT DOES NOT CREATE AN
     ATTORNEY-CLIENT RELATIONSHIP. CREATIVE COMMONS PROVIDES THIS
     INFORMATION ON AN "AS-IS" BASIS. CREATIVE COMMONS MAKES NO WARRANTIES
     REGARDING THE USE OF THIS DOCUMENT OR THE INFORMATION OR WORKS
     PROVIDED HEREUNDER, AND DISCLAIMS LIABILITY FOR DAMAGES RESULTING
     FROM THE USE OF THIS DOCUMENT OR THE INFORMATION OR WORKS PROVIDED
     HEREUNDER.
**** Statement of Purpose ***
The laws of most jurisdictions throughout the world automatically confer
exclusive Copyright and Related Rights (defined below) upon the creator and
subsequent owner(s) (each and all, an "owner") of an original work of
authorship and/or a database (each, a "Work").
Certain owners wish to permanently relinquish those rights to a Work for the
purpose of contributing to a commons of creative, cultural and scientific works
("Commons") that the public can reliably and without fear of later claims of
infringement build upon, modify, incorporate in other works, reuse and
redistribute as freely as possible in any form whatsoever and for any purposes,
including without limitation commercial purposes. These owners may contribute
to the Commons to promote the ideal of a free culture and the further
production of creative, cultural and scientific works, or to gain reputation or
greater distribution for their Work in part through the use and efforts of
others.
For these and/or other purposes and motivations, and without any expectation of
additional consideration or compensation, the person associating CC0 with a
Work (the "Affirmer"), to the extent that he or she is an owner of Copyright
and Related Rights in the Work, voluntarily elects to apply CC0 to the Work and
publicly distribute the Work under its terms, with knowledge of his or her
Copyright and Related Rights in the Work and the meaning and intended legal
effect of CC0 on those rights.
1. Copyright and Related Rights. A Work made available under CC0 may be
protected by copyright and related or neighboring rights ("Copyright and
Related Rights"). Copyright and Related Rights include, but are not limited to,
the following:
   i. the right to reproduce, adapt, distribute, perform, display, communicate,
      and translate a Work;
  ii. moral rights retained by the original author(s) and/or performer(s);
 iii. publicity and privacy rights pertaining to a person's image or likeness
      depicted in a Work;
  iv. rights protecting against unfair competition in regards to a Work,
      subject to the limitations in paragraph 4(a), below;
   v. rights protecting the extraction, dissemination, use and reuse of data in
      a Work;
  vi. database rights (such as those arising under Directive 96/9/EC of the
      European Parliament and of the Council of 11 March 1996 on the legal
      protection of databases, and under any national implementation thereof,
      including any amended or successor version of such directive); and
 vii. other similar, equivalent or corresponding rights throughout the world
      based on applicable law or treaty, and any national implementations
      thereof.
2. Waiver. To the greatest extent permitted by, but not in contravention of,
applicable law, Affirmer hereby overtly, fully, permanently, irrevocably and
unconditionally waives, abandons, and surrenders all of Affirmer's Copyright
and Related Rights and associated claims and causes of action, whether now
known or unknown (including existing as well as future claims and causes of
action), in the Work (i) in all territories worldwide, (ii) for the maximum
duration provided by applicable law or treaty (including future time
extensions), (iii) in any current or future medium and for any number of
copies, and (iv) for any purpose whatsoever, including without limitation
commercial, advertising or promotional purposes (the "Waiver"). Affirmer makes
the Waiver for the benefit of each member of the public at large and to the
detriment of Affirmer's heirs and successors, fully intending that such Waiver
shall not be subject to revocation, rescission, cancellation, termination, or
any other legal or equitable action to disrupt the quiet enjoyment of the Work
by the public as contemplated by Affirmer's express Statement of Purpose.
3. Public License Fallback. Should any part of the Waiver for any reason be
judged legally invalid or ineffective under applicable law, then the Waiver
shall be preserved to the maximum extent permitted taking into account
Affirmer's express Statement of Purpose. In addition, to the extent the Waiver
is so judged Affirmer hereby grants to each affected person a royalty-free, non
transferable, non sublicensable, non exclusive, irrevocable and unconditional
license to exercise Affirmer's Copyright and Related Rights in the Work (i) in
all territories worldwide, (ii) for the maximum duration provided by applicable
law or treaty (including future time extensions), (iii) in any current or
future medium and for any number of copies, and (iv) for any purpose
whatsoever, including without limitation commercial, advertising or promotional
purposes (the "License"). The License shall be deemed effective as of the date
CC0 was applied by Affirmer to the Work. Should any part of the License for any
reason be judged legally invalid or ineffective under applicable law, such
partial invalidity or ineffectiveness shall not invalidate the remainder of the
License, and in such case Affirmer hereby affirms that he or she will not (i)
exercise any of his or her remaining Copyright and Related Rights in the Work
or (ii) assert any associated claims and causes of action with respect to the
Work, in either case contrary to Affirmer's express Statement of Purpose.
4. Limitations and Disclaimers.
   a. No trademark or patent rights held by Affirmer are waived, abandoned,
      surrendered, licensed or otherwise affected by this document.
   b. Affirmer offers the Work as-is and makes no representations or warranties
      of any kind concerning the Work, express, implied, statutory or
      otherwise, including without limitation warranties of title,
      merchantability, fitness for a particular purpose, non infringement, or
      the absence of latent or other defects, accuracy, or the present or
      absence of errors, whether or not discoverable, all to the greatest
      extent permissible under applicable law.
   c. Affirmer disclaims responsibility for clearing rights of other persons
      that may apply to the Work or any use thereof, including without
      limitation any person's Copyright and Related Rights in the Work.
      Further, Affirmer disclaims responsibility for obtaining any necessary
      consents, permissions or other rights required for any use of the Work.
   d. Affirmer understands and acknowledges that Creative Commons is not a
      party to this document and has no duty or obligation with respect to this
      CC0 or use of the Work.
''',
	'CC-BY v3.0':       '''


                               Creative_Commons
****** Creative Commons Legal Code ******
***** Attribution 3.0 Unported *****
     CREATIVE COMMONS CORPORATION IS NOT A LAW FIRM AND DOES NOT PROVIDE
     LEGAL SERVICES. DISTRIBUTION OF THIS LICENSE DOES NOT CREATE AN
     ATTORNEY-CLIENT RELATIONSHIP. CREATIVE COMMONS PROVIDES THIS
     INFORMATION ON AN "AS-IS" BASIS. CREATIVE COMMONS MAKES NO WARRANTIES
     REGARDING THE INFORMATION PROVIDED, AND DISCLAIMS LIABILITY FOR
     DAMAGES RESULTING FROM ITS USE.
**** License ****
THE WORK (AS DEFINED BELOW) IS PROVIDED UNDER THE TERMS OF THIS CREATIVE
COMMONS PUBLIC LICENSE ("CCPL" OR "LICENSE"). THE WORK IS PROTECTED BY
COPYRIGHT AND/OR OTHER APPLICABLE LAW. ANY USE OF THE WORK OTHER THAN AS
AUTHORIZED UNDER THIS LICENSE OR COPYRIGHT LAW IS PROHIBITED.
BY EXERCISING ANY RIGHTS TO THE WORK PROVIDED HERE, YOU ACCEPT AND AGREE TO BE
BOUND BY THE TERMS OF THIS LICENSE. TO THE EXTENT THIS LICENSE MAY BE
CONSIDERED TO BE A CONTRACT, THE LICENSOR GRANTS YOU THE RIGHTS CONTAINED HERE
IN CONSIDERATION OF YOUR ACCEPTANCE OF SUCH TERMS AND CONDITIONS.
1. Definitions
   a. "Adaptation" means a work based upon the Work, or upon the Work and other
      pre-existing works, such as a translation, adaptation, derivative work,
      arrangement of music or other alterations of a literary or artistic work,
      or phonogram or performance and includes cinematographic adaptations or
      any other form in which the Work may be recast, transformed, or adapted
      including in any form recognizably derived from the original, except that
      a work that constitutes a Collection will not be considered an Adaptation
      for the purpose of this License. For the avoidance of doubt, where the
      Work is a musical work, performance or phonogram, the synchronization of
      the Work in timed-relation with a moving image ("synching") will be
      considered an Adaptation for the purpose of this License.
   b. "Collection" means a collection of literary or artistic works, such as
      encyclopedias and anthologies, or performances, phonograms or broadcasts,
      or other works or subject matter other than works listed in Section 1(f)
      below, which, by reason of the selection and arrangement of their
      contents, constitute intellectual creations, in which the Work is
      included in its entirety in unmodified form along with one or more other
      contributions, each constituting separate and independent works in
      themselves, which together are assembled into a collective whole. A work
      that constitutes a Collection will not be considered an Adaptation (as
      defined above) for the purposes of this License.
   c. "Distribute" means to make available to the public the original and
      copies of the Work or Adaptation, as appropriate, through sale or other
      transfer of ownership.
   d. "Licensor" means the individual, individuals, entity or entities that
      offer(s) the Work under the terms of this License.
   e. "Original Author" means, in the case of a literary or artistic work, the
      individual, individuals, entity or entities who created the Work or if no
      individual or entity can be identified, the publisher; and in addition
      (i) in the case of a performance the actors, singers, musicians, dancers,
      and other persons who act, sing, deliver, declaim, play in, interpret or
      otherwise perform literary or artistic works or expressions of folklore;
      (ii) in the case of a phonogram the producer being the person or legal
      entity who first fixes the sounds of a performance or other sounds; and,
      (iii) in the case of broadcasts, the organization that transmits the
      broadcast.
   f. "Work" means the literary and/or artistic work offered under the terms of
      this License including without limitation any production in the literary,
      scientific and artistic domain, whatever may be the mode or form of its
      expression including digital form, such as a book, pamphlet and other
      writing; a lecture, address, sermon or other work of the same nature; a
      dramatic or dramatico-musical work; a choreographic work or entertainment
      in dumb show; a musical composition with or without words; a
      cinematographic work to which are assimilated works expressed by a
      process analogous to cinematography; a work of drawing, painting,
      architecture, sculpture, engraving or lithography; a photographic work to
      which are assimilated works expressed by a process analogous to
      photography; a work of applied art; an illustration, map, plan, sketch or
      three-dimensional work relative to geography, topography, architecture or
      science; a performance; a broadcast; a phonogram; a compilation of data
      to the extent it is protected as a copyrightable work; or a work
      performed by a variety or circus performer to the extent it is not
      otherwise considered a literary or artistic work.
   g. "You" means an individual or entity exercising rights under this License
      who has not previously violated the terms of this License with respect to
      the Work, or who has received express permission from the Licensor to
      exercise rights under this License despite a previous violation.
   h. "Publicly Perform" means to perform public recitations of the Work and to
      communicate to the public those public recitations, by any means or
      process, including by wire or wireless means or public digital
      performances; to make available to the public Works in such a way that
      members of the public may access these Works from a place and at a place
      individually chosen by them; to perform the Work to the public by any
      means or process and the communication to the public of the performances
      of the Work, including by public digital performance; to broadcast and
      rebroadcast the Work by any means including signs, sounds or images.
   i. "Reproduce" means to make copies of the Work by any means including
      without limitation by sound or visual recordings and the right of
      fixation and reproducing fixations of the Work, including storage of a
      protected performance or phonogram in digital form or other electronic
      medium.
2. Fair Dealing Rights. Nothing in this License is intended to reduce, limit,
or restrict any uses free from copyright or rights arising from limitations or
exceptions that are provided for in connection with the copyright protection
under copyright law or other applicable laws.
3. License Grant. Subject to the terms and conditions of this License, Licensor
hereby grants You a worldwide, royalty-free, non-exclusive, perpetual (for the
duration of the applicable copyright) license to exercise the rights in the
Work as stated below:
   a. to Reproduce the Work, to incorporate the Work into one or more
      Collections, and to Reproduce the Work as incorporated in the
      Collections;
   b. to create and Reproduce Adaptations provided that any such Adaptation,
      including any translation in any medium, takes reasonable steps to
      clearly label, demarcate or otherwise identify that changes were made to
      the original Work. For example, a translation could be marked "The
      original work was translated from English to Spanish," or a modification
      could indicate "The original work has been modified.";
   c. to Distribute and Publicly Perform the Work including as incorporated in
      Collections; and,
   d. to Distribute and Publicly Perform Adaptations.
   e. For the avoidance of doubt:
         i. Non-waivable Compulsory License Schemes. In those jurisdictions in
            which the right to collect royalties through any statutory or
            compulsory licensing scheme cannot be waived, the Licensor reserves
            the exclusive right to collect such royalties for any exercise by
            You of the rights granted under this License;
        ii. Waivable Compulsory License Schemes. In those jurisdictions in
            which the right to collect royalties through any statutory or
            compulsory licensing scheme can be waived, the Licensor waives the
            exclusive right to collect such royalties for any exercise by You
            of the rights granted under this License; and,
       iii. Voluntary License Schemes. The Licensor waives the right to collect
            royalties, whether individually or, in the event that the Licensor
            is a member of a collecting society that administers voluntary
            licensing schemes, via that society, from any exercise by You of
            the rights granted under this License.
The above rights may be exercised in all media and formats whether now known or
hereafter devised. The above rights include the right to make such
modifications as are technically necessary to exercise the rights in other
media and formats. Subject to Section 8(f), all rights not expressly granted by
Licensor are hereby reserved.
4. Restrictions. The license granted in Section 3 above is expressly made
subject to and limited by the following restrictions:
   a. You may Distribute or Publicly Perform the Work only under the terms of
      this License. You must include a copy of, or the Uniform Resource
      Identifier (URI) for, this License with every copy of the Work You
      Distribute or Publicly Perform. You may not offer or impose any terms on
      the Work that restrict the terms of this License or the ability of the
      recipient of the Work to exercise the rights granted to that recipient
      under the terms of the License. You may not sublicense the Work. You must
      keep intact all notices that refer to this License and to the disclaimer
      of warranties with every copy of the Work You Distribute or Publicly
      Perform. When You Distribute or Publicly Perform the Work, You may not
      impose any effective technological measures on the Work that restrict the
      ability of a recipient of the Work from You to exercise the rights
      granted to that recipient under the terms of the License. This Section 4
      (a) applies to the Work as incorporated in a Collection, but this does
      not require the Collection apart from the Work itself to be made subject
      to the terms of this License. If You create a Collection, upon notice
      from any Licensor You must, to the extent practicable, remove from the
      Collection any credit as required by Section 4(b), as requested. If You
      create an Adaptation, upon notice from any Licensor You must, to the
      extent practicable, remove from the Adaptation any credit as required by
      Section 4(b), as requested.
   b. If You Distribute, or Publicly Perform the Work or any Adaptations or
      Collections, You must, unless a request has been made pursuant to Section
      4(a), keep intact all copyright notices for the Work and provide,
      reasonable to the medium or means You are utilizing: (i) the name of the
      Original Author (or pseudonym, if applicable) if supplied, and/or if the
      Original Author and/or Licensor designate another party or parties (e.g.,
      a sponsor institute, publishing entity, journal) for attribution
      ("Attribution Parties") in Licensor's copyright notice, terms of service
      or by other reasonable means, the name of such party or parties; (ii) the
      title of the Work if supplied; (iii) to the extent reasonably
      practicable, the URI, if any, that Licensor specifies to be associated
      with the Work, unless such URI does not refer to the copyright notice or
      licensing information for the Work; and (iv) , consistent with Section 3
      (b), in the case of an Adaptation, a credit identifying the use of the
      Work in the Adaptation (e.g., "French translation of the Work by Original
      Author," or "Screenplay based on original Work by Original Author"). The
      credit required by this Section 4 (b) may be implemented in any
      reasonable manner; provided, however, that in the case of a Adaptation or
      Collection, at a minimum such credit will appear, if a credit for all
      contributing authors of the Adaptation or Collection appears, then as
      part of these credits and in a manner at least as prominent as the
      credits for the other contributing authors. For the avoidance of doubt,
      You may only use the credit required by this Section for the purpose of
      attribution in the manner set out above and, by exercising Your rights
      under this License, You may not implicitly or explicitly assert or imply
      any connection with, sponsorship or endorsement by the Original Author,
      Licensor and/or Attribution Parties, as appropriate, of You or Your use
      of the Work, without the separate, express prior written permission of
      the Original Author, Licensor and/or Attribution Parties.
   c. Except as otherwise agreed in writing by the Licensor or as may be
      otherwise permitted by applicable law, if You Reproduce, Distribute or
      Publicly Perform the Work either by itself or as part of any Adaptations
      or Collections, You must not distort, mutilate, modify or take other
      derogatory action in relation to the Work which would be prejudicial to
      the Original Author's honor or reputation. Licensor agrees that in those
      jurisdictions (e.g. Japan), in which any exercise of the right granted in
      Section 3(b) of this License (the right to make Adaptations) would be
      deemed to be a distortion, mutilation, modification or other derogatory
      action prejudicial to the Original Author's honor and reputation, the
      Licensor will waive or not assert, as appropriate, this Section, to the
      fullest extent permitted by the applicable national law, to enable You to
      reasonably exercise Your right under Section 3(b) of this License (right
      to make Adaptations) but not otherwise.
5. Representations, Warranties and Disclaimer
UNLESS OTHERWISE MUTUALLY AGREED TO BY THE PARTIES IN WRITING, LICENSOR OFFERS
THE WORK AS-IS AND MAKES NO REPRESENTATIONS OR WARRANTIES OF ANY KIND
CONCERNING THE WORK, EXPRESS, IMPLIED, STATUTORY OR OTHERWISE, INCLUDING,
WITHOUT LIMITATION, WARRANTIES OF TITLE, MERCHANTIBILITY, FITNESS FOR A
PARTICULAR PURPOSE, NONINFRINGEMENT, OR THE ABSENCE OF LATENT OR OTHER DEFECTS,
ACCURACY, OR THE PRESENCE OF ABSENCE OF ERRORS, WHETHER OR NOT DISCOVERABLE.
SOME JURISDICTIONS DO NOT ALLOW THE EXCLUSION OF IMPLIED WARRANTIES, SO SUCH
EXCLUSION MAY NOT APPLY TO YOU.
6. Limitation on Liability. EXCEPT TO THE EXTENT REQUIRED BY APPLICABLE LAW, IN
NO EVENT WILL LICENSOR BE LIABLE TO YOU ON ANY LEGAL THEORY FOR ANY SPECIAL,
INCIDENTAL, CONSEQUENTIAL, PUNITIVE OR EXEMPLARY DAMAGES ARISING OUT OF THIS
LICENSE OR THE USE OF THE WORK, EVEN IF LICENSOR HAS BEEN ADVISED OF THE
POSSIBILITY OF SUCH DAMAGES.
7. Termination
   a. This License and the rights granted hereunder will terminate
      automatically upon any breach by You of the terms of this License.
      Individuals or entities who have received Adaptations or Collections from
      You under this License, however, will not have their licenses terminated
      provided such individuals or entities remain in full compliance with
      those licenses. Sections 1, 2, 5, 6, 7, and 8 will survive any
      termination of this License.
   b. Subject to the above terms and conditions, the license granted here is
      perpetual (for the duration of the applicable copyright in the Work).
      Notwithstanding the above, Licensor reserves the right to release the
      Work under different license terms or to stop distributing the Work at
      any time; provided, however that any such election will not serve to
      withdraw this License (or any other license that has been, or is required
      to be, granted under the terms of this License), and this License will
      continue in full force and effect unless terminated as stated above.
8. Miscellaneous
   a. Each time You Distribute or Publicly Perform the Work or a Collection,
      the Licensor offers to the recipient a license to the Work on the same
      terms and conditions as the license granted to You under this License.
   b. Each time You Distribute or Publicly Perform an Adaptation, Licensor
      offers to the recipient a license to the original Work on the same terms
      and conditions as the license granted to You under this License.
   c. If any provision of this License is invalid or unenforceable under
      applicable law, it shall not affect the validity or enforceability of the
      remainder of the terms of this License, and without further action by the
      parties to this agreement, such provision shall be reformed to the
      minimum extent necessary to make such provision valid and enforceable.
   d. No term or provision of this License shall be deemed waived and no breach
      consented to unless such waiver or consent shall be in writing and signed
      by the party to be charged with such waiver or consent.
   e. This License constitutes the entire agreement between the parties with
      respect to the Work licensed here. There are no understandings,
      agreements or representations with respect to the Work not specified
      here. Licensor shall not be bound by any additional provisions that may
      appear in any communication from You. This License may not be modified
      without the mutual written agreement of the Licensor and You.
   f. The rights granted under, and the subject matter referenced, in this
      License were drafted utilizing the terminology of the Berne Convention
      for the Protection of Literary and Artistic Works (as amended on
      September 28, 1979), the Rome Convention of 1961, the WIPO Copyright
      Treaty of 1996, the WIPO Performances and Phonograms Treaty of 1996 and
      the Universal Copyright Convention (as revised on July 24, 1971). These
      rights and subject matter take effect in the relevant jurisdiction in
      which the License terms are sought to be enforced according to the
      corresponding provisions of the implementation of those treaty provisions
      in the applicable national law. If the standard suite of rights granted
      under applicable copyright law includes additional rights not granted
      under this License, such additional rights are deemed to be included in
      the License; this License is not intended to restrict the license of any
      rights under applicable law.
     **** Creative Commons Notice ****
     Creative Commons is not a party to this License, and makes no
     warranty whatsoever in connection with the Work. Creative Commons
     will not be liable to You or any party on any legal theory for any
     damages whatsoever, including without limitation any general,
     special, incidental or consequential damages arising in connection to
     this license. Notwithstanding the foregoing two (2) sentences, if
     Creative Commons has expressly identified itself as the Licensor
     hereunder, it shall have all rights and obligations of Licensor.
     Except for the limited purpose of indicating to the public that the
     Work is licensed under the CCPL, Creative Commons does not authorize
     the use by either party of the trademark "Creative Commons" or any
     related trademark or logo of Creative Commons without the prior
     written consent of Creative Commons. Any permitted use will be in
     compliance with Creative Commons' then-current trademark usage
     guidelines, as may be published on its website or otherwise made
     available upon request from time to time. For the avoidance of doubt,
     this trademark restriction does not form part of this License.
     Creative Commons may be contacted at http://creativecommons.org/.
''',
	'CC-BY-SA v3.0':    '''


                               Creative_Commons
****** Creative Commons Legal Code ******
***** Attribution-ShareAlike 3.0 Unported *****
     CREATIVE COMMONS CORPORATION IS NOT A LAW FIRM AND DOES NOT PROVIDE
     LEGAL SERVICES. DISTRIBUTION OF THIS LICENSE DOES NOT CREATE AN
     ATTORNEY-CLIENT RELATIONSHIP. CREATIVE COMMONS PROVIDES THIS
     INFORMATION ON AN "AS-IS" BASIS. CREATIVE COMMONS MAKES NO WARRANTIES
     REGARDING THE INFORMATION PROVIDED, AND DISCLAIMS LIABILITY FOR
     DAMAGES RESULTING FROM ITS USE.
**** License ****
THE WORK (AS DEFINED BELOW) IS PROVIDED UNDER THE TERMS OF THIS CREATIVE
COMMONS PUBLIC LICENSE ("CCPL" OR "LICENSE"). THE WORK IS PROTECTED BY
COPYRIGHT AND/OR OTHER APPLICABLE LAW. ANY USE OF THE WORK OTHER THAN AS
AUTHORIZED UNDER THIS LICENSE OR COPYRIGHT LAW IS PROHIBITED.
BY EXERCISING ANY RIGHTS TO THE WORK PROVIDED HERE, YOU ACCEPT AND AGREE TO BE
BOUND BY THE TERMS OF THIS LICENSE. TO THE EXTENT THIS LICENSE MAY BE
CONSIDERED TO BE A CONTRACT, THE LICENSOR GRANTS YOU THE RIGHTS CONTAINED HERE
IN CONSIDERATION OF YOUR ACCEPTANCE OF SUCH TERMS AND CONDITIONS.
1. Definitions
   a. "Adaptation" means a work based upon the Work, or upon the Work and other
      pre-existing works, such as a translation, adaptation, derivative work,
      arrangement of music or other alterations of a literary or artistic work,
      or phonogram or performance and includes cinematographic adaptations or
      any other form in which the Work may be recast, transformed, or adapted
      including in any form recognizably derived from the original, except that
      a work that constitutes a Collection will not be considered an Adaptation
      for the purpose of this License. For the avoidance of doubt, where the
      Work is a musical work, performance or phonogram, the synchronization of
      the Work in timed-relation with a moving image ("synching") will be
      considered an Adaptation for the purpose of this License.
   b. "Collection" means a collection of literary or artistic works, such as
      encyclopedias and anthologies, or performances, phonograms or broadcasts,
      or other works or subject matter other than works listed in Section 1(f)
      below, which, by reason of the selection and arrangement of their
      contents, constitute intellectual creations, in which the Work is
      included in its entirety in unmodified form along with one or more other
      contributions, each constituting separate and independent works in
      themselves, which together are assembled into a collective whole. A work
      that constitutes a Collection will not be considered an Adaptation (as
      defined below) for the purposes of this License.
   c. "Creative Commons Compatible License" means a license that is listed at
      http://creativecommons.org/compatiblelicenses that has been approved by
      Creative Commons as being essentially equivalent to this License,
      including, at a minimum, because that license: (i) contains terms that
      have the same purpose, meaning and effect as the License Elements of this
      License; and, (ii) explicitly permits the relicensing of adaptations of
      works made available under that license under this License or a Creative
      Commons jurisdiction license with the same License Elements as this
      License.
   d. "Distribute" means to make available to the public the original and
      copies of the Work or Adaptation, as appropriate, through sale or other
      transfer of ownership.
   e. "License Elements" means the following high-level license attributes as
      selected by Licensor and indicated in the title of this License:
      Attribution, ShareAlike.
   f. "Licensor" means the individual, individuals, entity or entities that
      offer(s) the Work under the terms of this License.
   g. "Original Author" means, in the case of a literary or artistic work, the
      individual, individuals, entity or entities who created the Work or if no
      individual or entity can be identified, the publisher; and in addition
      (i) in the case of a performance the actors, singers, musicians, dancers,
      and other persons who act, sing, deliver, declaim, play in, interpret or
      otherwise perform literary or artistic works or expressions of folklore;
      (ii) in the case of a phonogram the producer being the person or legal
      entity who first fixes the sounds of a performance or other sounds; and,
      (iii) in the case of broadcasts, the organization that transmits the
      broadcast.
   h. "Work" means the literary and/or artistic work offered under the terms of
      this License including without limitation any production in the literary,
      scientific and artistic domain, whatever may be the mode or form of its
      expression including digital form, such as a book, pamphlet and other
      writing; a lecture, address, sermon or other work of the same nature; a
      dramatic or dramatico-musical work; a choreographic work or entertainment
      in dumb show; a musical composition with or without words; a
      cinematographic work to which are assimilated works expressed by a
      process analogous to cinematography; a work of drawing, painting,
      architecture, sculpture, engraving or lithography; a photographic work to
      which are assimilated works expressed by a process analogous to
      photography; a work of applied art; an illustration, map, plan, sketch or
      three-dimensional work relative to geography, topography, architecture or
      science; a performance; a broadcast; a phonogram; a compilation of data
      to the extent it is protected as a copyrightable work; or a work
      performed by a variety or circus performer to the extent it is not
      otherwise considered a literary or artistic work.
   i. "You" means an individual or entity exercising rights under this License
      who has not previously violated the terms of this License with respect to
      the Work, or who has received express permission from the Licensor to
      exercise rights under this License despite a previous violation.
   j. "Publicly Perform" means to perform public recitations of the Work and to
      communicate to the public those public recitations, by any means or
      process, including by wire or wireless means or public digital
      performances; to make available to the public Works in such a way that
      members of the public may access these Works from a place and at a place
      individually chosen by them; to perform the Work to the public by any
      means or process and the communication to the public of the performances
      of the Work, including by public digital performance; to broadcast and
      rebroadcast the Work by any means including signs, sounds or images.
   k. "Reproduce" means to make copies of the Work by any means including
      without limitation by sound or visual recordings and the right of
      fixation and reproducing fixations of the Work, including storage of a
      protected performance or phonogram in digital form or other electronic
      medium.
2. Fair Dealing Rights. Nothing in this License is intended to reduce, limit,
or restrict any uses free from copyright or rights arising from limitations or
exceptions that are provided for in connection with the copyright protection
under copyright law or other applicable laws.
3. License Grant. Subject to the terms and conditions of this License, Licensor
hereby grants You a worldwide, royalty-free, non-exclusive, perpetual (for the
duration of the applicable copyright) license to exercise the rights in the
Work as stated below:
   a. to Reproduce the Work, to incorporate the Work into one or more
      Collections, and to Reproduce the Work as incorporated in the
      Collections;
   b. to create and Reproduce Adaptations provided that any such Adaptation,
      including any translation in any medium, takes reasonable steps to
      clearly label, demarcate or otherwise identify that changes were made to
      the original Work. For example, a translation could be marked "The
      original work was translated from English to Spanish," or a modification
      could indicate "The original work has been modified.";
   c. to Distribute and Publicly Perform the Work including as incorporated in
      Collections; and,
   d. to Distribute and Publicly Perform Adaptations.
   e. For the avoidance of doubt:
         i. Non-waivable Compulsory License Schemes. In those jurisdictions in
            which the right to collect royalties through any statutory or
            compulsory licensing scheme cannot be waived, the Licensor reserves
            the exclusive right to collect such royalties for any exercise by
            You of the rights granted under this License;
        ii. Waivable Compulsory License Schemes. In those jurisdictions in
            which the right to collect royalties through any statutory or
            compulsory licensing scheme can be waived, the Licensor waives the
            exclusive right to collect such royalties for any exercise by You
            of the rights granted under this License; and,
       iii. Voluntary License Schemes. The Licensor waives the right to collect
            royalties, whether individually or, in the event that the Licensor
            is a member of a collecting society that administers voluntary
            licensing schemes, via that society, from any exercise by You of
            the rights granted under this License.
The above rights may be exercised in all media and formats whether now known or
hereafter devised. The above rights include the right to make such
modifications as are technically necessary to exercise the rights in other
media and formats. Subject to Section 8(f), all rights not expressly granted by
Licensor are hereby reserved.
4. Restrictions. The license granted in Section 3 above is expressly made
subject to and limited by the following restrictions:
   a. You may Distribute or Publicly Perform the Work only under the terms of
      this License. You must include a copy of, or the Uniform Resource
      Identifier (URI) for, this License with every copy of the Work You
      Distribute or Publicly Perform. You may not offer or impose any terms on
      the Work that restrict the terms of this License or the ability of the
      recipient of the Work to exercise the rights granted to that recipient
      under the terms of the License. You may not sublicense the Work. You must
      keep intact all notices that refer to this License and to the disclaimer
      of warranties with every copy of the Work You Distribute or Publicly
      Perform. When You Distribute or Publicly Perform the Work, You may not
      impose any effective technological measures on the Work that restrict the
      ability of a recipient of the Work from You to exercise the rights
      granted to that recipient under the terms of the License. This Section 4
      (a) applies to the Work as incorporated in a Collection, but this does
      not require the Collection apart from the Work itself to be made subject
      to the terms of this License. If You create a Collection, upon notice
      from any Licensor You must, to the extent practicable, remove from the
      Collection any credit as required by Section 4(c), as requested. If You
      create an Adaptation, upon notice from any Licensor You must, to the
      extent practicable, remove from the Adaptation any credit as required by
      Section 4(c), as requested.
   b. You may Distribute or Publicly Perform an Adaptation only under the terms
      of: (i) this License; (ii) a later version of this License with the same
      License Elements as this License; (iii) a Creative Commons jurisdiction
      license (either this or a later license version) that contains the same
      License Elements as this License (e.g., Attribution-ShareAlike 3.0 US));
      (iv) a Creative Commons Compatible License. If you license the Adaptation
      under one of the licenses mentioned in (iv), you must comply with the
      terms of that license. If you license the Adaptation under the terms of
      any of the licenses mentioned in (i), (ii) or (iii) (the "Applicable
      License"), you must comply with the terms of the Applicable License
      generally and the following provisions: (I) You must include a copy of,
      or the URI for, the Applicable License with every copy of each Adaptation
      You Distribute or Publicly Perform; (II) You may not offer or impose any
      terms on the Adaptation that restrict the terms of the Applicable License
      or the ability of the recipient of the Adaptation to exercise the rights
      granted to that recipient under the terms of the Applicable License;
      (III) You must keep intact all notices that refer to the Applicable
      License and to the disclaimer of warranties with every copy of the Work
      as included in the Adaptation You Distribute or Publicly Perform; (IV)
      when You Distribute or Publicly Perform the Adaptation, You may not
      impose any effective technological measures on the Adaptation that
      restrict the ability of a recipient of the Adaptation from You to
      exercise the rights granted to that recipient under the terms of the
      Applicable License. This Section 4(b) applies to the Adaptation as
      incorporated in a Collection, but this does not require the Collection
      apart from the Adaptation itself to be made subject to the terms of the
      Applicable License.
   c. If You Distribute, or Publicly Perform the Work or any Adaptations or
      Collections, You must, unless a request has been made pursuant to Section
      4(a), keep intact all copyright notices for the Work and provide,
      reasonable to the medium or means You are utilizing: (i) the name of the
      Original Author (or pseudonym, if applicable) if supplied, and/or if the
      Original Author and/or Licensor designate another party or parties (e.g.,
      a sponsor institute, publishing entity, journal) for attribution
      ("Attribution Parties") in Licensor's copyright notice, terms of service
      or by other reasonable means, the name of such party or parties; (ii) the
      title of the Work if supplied; (iii) to the extent reasonably
      practicable, the URI, if any, that Licensor specifies to be associated
      with the Work, unless such URI does not refer to the copyright notice or
      licensing information for the Work; and (iv) , consistent with Ssection 3
      (b), in the case of an Adaptation, a credit identifying the use of the
      Work in the Adaptation (e.g., "French translation of the Work by Original
      Author," or "Screenplay based on original Work by Original Author"). The
      credit required by this Section 4(c) may be implemented in any reasonable
      manner; provided, however, that in the case of a Adaptation or
      Collection, at a minimum such credit will appear, if a credit for all
      contributing authors of the Adaptation or Collection appears, then as
      part of these credits and in a manner at least as prominent as the
      credits for the other contributing authors. For the avoidance of doubt,
      You may only use the credit required by this Section for the purpose of
      attribution in the manner set out above and, by exercising Your rights
      under this License, You may not implicitly or explicitly assert or imply
      any connection with, sponsorship or endorsement by the Original Author,
      Licensor and/or Attribution Parties, as appropriate, of You or Your use
      of the Work, without the separate, express prior written permission of
      the Original Author, Licensor and/or Attribution Parties.
   d. Except as otherwise agreed in writing by the Licensor or as may be
      otherwise permitted by applicable law, if You Reproduce, Distribute or
      Publicly Perform the Work either by itself or as part of any Adaptations
      or Collections, You must not distort, mutilate, modify or take other
      derogatory action in relation to the Work which would be prejudicial to
      the Original Author's honor or reputation. Licensor agrees that in those
      jurisdictions (e.g. Japan), in which any exercise of the right granted in
      Section 3(b) of this License (the right to make Adaptations) would be
      deemed to be a distortion, mutilation, modification or other derogatory
      action prejudicial to the Original Author's honor and reputation, the
      Licensor will waive or not assert, as appropriate, this Section, to the
      fullest extent permitted by the applicable national law, to enable You to
      reasonably exercise Your right under Section 3(b) of this License (right
      to make Adaptations) but not otherwise.
5. Representations, Warranties and Disclaimer
UNLESS OTHERWISE MUTUALLY AGREED TO BY THE PARTIES IN WRITING, LICENSOR OFFERS
THE WORK AS-IS AND MAKES NO REPRESENTATIONS OR WARRANTIES OF ANY KIND
CONCERNING THE WORK, EXPRESS, IMPLIED, STATUTORY OR OTHERWISE, INCLUDING,
WITHOUT LIMITATION, WARRANTIES OF TITLE, MERCHANTIBILITY, FITNESS FOR A
PARTICULAR PURPOSE, NONINFRINGEMENT, OR THE ABSENCE OF LATENT OR OTHER DEFECTS,
ACCURACY, OR THE PRESENCE OF ABSENCE OF ERRORS, WHETHER OR NOT DISCOVERABLE.
SOME JURISDICTIONS DO NOT ALLOW THE EXCLUSION OF IMPLIED WARRANTIES, SO SUCH
EXCLUSION MAY NOT APPLY TO YOU.
6. Limitation on Liability. EXCEPT TO THE EXTENT REQUIRED BY APPLICABLE LAW, IN
NO EVENT WILL LICENSOR BE LIABLE TO YOU ON ANY LEGAL THEORY FOR ANY SPECIAL,
INCIDENTAL, CONSEQUENTIAL, PUNITIVE OR EXEMPLARY DAMAGES ARISING OUT OF THIS
LICENSE OR THE USE OF THE WORK, EVEN IF LICENSOR HAS BEEN ADVISED OF THE
POSSIBILITY OF SUCH DAMAGES.
7. Termination
   a. This License and the rights granted hereunder will terminate
      automatically upon any breach by You of the terms of this License.
      Individuals or entities who have received Adaptations or Collections from
      You under this License, however, will not have their licenses terminated
      provided such individuals or entities remain in full compliance with
      those licenses. Sections 1, 2, 5, 6, 7, and 8 will survive any
      termination of this License.
   b. Subject to the above terms and conditions, the license granted here is
      perpetual (for the duration of the applicable copyright in the Work).
      Notwithstanding the above, Licensor reserves the right to release the
      Work under different license terms or to stop distributing the Work at
      any time; provided, however that any such election will not serve to
      withdraw this License (or any other license that has been, or is required
      to be, granted under the terms of this License), and this License will
      continue in full force and effect unless terminated as stated above.
8. Miscellaneous
   a. Each time You Distribute or Publicly Perform the Work or a Collection,
      the Licensor offers to the recipient a license to the Work on the same
      terms and conditions as the license granted to You under this License.
   b. Each time You Distribute or Publicly Perform an Adaptation, Licensor
      offers to the recipient a license to the original Work on the same terms
      and conditions as the license granted to You under this License.
   c. If any provision of this License is invalid or unenforceable under
      applicable law, it shall not affect the validity or enforceability of the
      remainder of the terms of this License, and without further action by the
      parties to this agreement, such provision shall be reformed to the
      minimum extent necessary to make such provision valid and enforceable.
   d. No term or provision of this License shall be deemed waived and no breach
      consented to unless such waiver or consent shall be in writing and signed
      by the party to be charged with such waiver or consent.
   e. This License constitutes the entire agreement between the parties with
      respect to the Work licensed here. There are no understandings,
      agreements or representations with respect to the Work not specified
      here. Licensor shall not be bound by any additional provisions that may
      appear in any communication from You. This License may not be modified
      without the mutual written agreement of the Licensor and You.
   f. The rights granted under, and the subject matter referenced, in this
      License were drafted utilizing the terminology of the Berne Convention
      for the Protection of Literary and Artistic Works (as amended on
      September 28, 1979), the Rome Convention of 1961, the WIPO Copyright
      Treaty of 1996, the WIPO Performances and Phonograms Treaty of 1996 and
      the Universal Copyright Convention (as revised on July 24, 1971). These
      rights and subject matter take effect in the relevant jurisdiction in
      which the License terms are sought to be enforced according to the
      corresponding provisions of the implementation of those treaty provisions
      in the applicable national law. If the standard suite of rights granted
      under applicable copyright law includes additional rights not granted
      under this License, such additional rights are deemed to be included in
      the License; this License is not intended to restrict the license of any
      rights under applicable law.
     **** Creative Commons Notice ****
     Creative Commons is not a party to this License, and makes no
     warranty whatsoever in connection with the Work. Creative Commons
     will not be liable to You or any party on any legal theory for any
     damages whatsoever, including without limitation any general,
     special, incidental or consequential damages arising in connection to
     this license. Notwithstanding the foregoing two (2) sentences, if
     Creative Commons has expressly identified itself as the Licensor
     hereunder, it shall have all rights and obligations of Licensor.
     Except for the limited purpose of indicating to the public that the
     Work is licensed under the CCPL, Creative Commons does not authorize
     the use by either party of the trademark "Creative Commons" or any
     related trademark or logo of Creative Commons without the prior
     written consent of Creative Commons. Any permitted use will be in
     compliance with Creative Commons' then-current trademark usage
     guidelines, as may be published on its website or otherwise made
     available upon request from time to time. For the avoidance of doubt,
     this trademark restriction does not form part of the License.
     Creative Commons may be contacted at http://creativecommons.org/.
''',
	'CC-BY-NC-SA v3.0': '''


                               Creative_Commons
****** Creative Commons Legal Code ******
***** Attribution-NonCommercial-ShareAlike 3.0 Unported *****
     CREATIVE COMMONS CORPORATION IS NOT A LAW FIRM AND DOES NOT PROVIDE
     LEGAL SERVICES. DISTRIBUTION OF THIS LICENSE DOES NOT CREATE AN
     ATTORNEY-CLIENT RELATIONSHIP. CREATIVE COMMONS PROVIDES THIS
     INFORMATION ON AN "AS-IS" BASIS. CREATIVE COMMONS MAKES NO WARRANTIES
     REGARDING THE INFORMATION PROVIDED, AND DISCLAIMS LIABILITY FOR
     DAMAGES RESULTING FROM ITS USE.
**** License ****
THE WORK (AS DEFINED BELOW) IS PROVIDED UNDER THE TERMS OF THIS CREATIVE
COMMONS PUBLIC LICENSE ("CCPL" OR "LICENSE"). THE WORK IS PROTECTED BY
COPYRIGHT AND/OR OTHER APPLICABLE LAW. ANY USE OF THE WORK OTHER THAN AS
AUTHORIZED UNDER THIS LICENSE OR COPYRIGHT LAW IS PROHIBITED.
BY EXERCISING ANY RIGHTS TO THE WORK PROVIDED HERE, YOU ACCEPT AND AGREE TO BE
BOUND BY THE TERMS OF THIS LICENSE. TO THE EXTENT THIS LICENSE MAY BE
CONSIDERED TO BE A CONTRACT, THE LICENSOR GRANTS YOU THE RIGHTS CONTAINED HERE
IN CONSIDERATION OF YOUR ACCEPTANCE OF SUCH TERMS AND CONDITIONS.
1. Definitions
   a. "Adaptation" means a work based upon the Work, or upon the Work and other
      pre-existing works, such as a translation, adaptation, derivative work,
      arrangement of music or other alterations of a literary or artistic work,
      or phonogram or performance and includes cinematographic adaptations or
      any other form in which the Work may be recast, transformed, or adapted
      including in any form recognizably derived from the original, except that
      a work that constitutes a Collection will not be considered an Adaptation
      for the purpose of this License. For the avoidance of doubt, where the
      Work is a musical work, performance or phonogram, the synchronization of
      the Work in timed-relation with a moving image ("synching") will be
      considered an Adaptation for the purpose of this License.
   b. "Collection" means a collection of literary or artistic works, such as
      encyclopedias and anthologies, or performances, phonograms or broadcasts,
      or other works or subject matter other than works listed in Section 1(g)
      below, which, by reason of the selection and arrangement of their
      contents, constitute intellectual creations, in which the Work is
      included in its entirety in unmodified form along with one or more other
      contributions, each constituting separate and independent works in
      themselves, which together are assembled into a collective whole. A work
      that constitutes a Collection will not be considered an Adaptation (as
      defined above) for the purposes of this License.
   c. "Distribute" means to make available to the public the original and
      copies of the Work or Adaptation, as appropriate, through sale or other
      transfer of ownership.
   d. "License Elements" means the following high-level license attributes as
      selected by Licensor and indicated in the title of this License:
      Attribution, Noncommercial, ShareAlike.
   e. "Licensor" means the individual, individuals, entity or entities that
      offer(s) the Work under the terms of this License.
   f. "Original Author" means, in the case of a literary or artistic work, the
      individual, individuals, entity or entities who created the Work or if no
      individual or entity can be identified, the publisher; and in addition
      (i) in the case of a performance the actors, singers, musicians, dancers,
      and other persons who act, sing, deliver, declaim, play in, interpret or
      otherwise perform literary or artistic works or expressions of folklore;
      (ii) in the case of a phonogram the producer being the person or legal
      entity who first fixes the sounds of a performance or other sounds; and,
      (iii) in the case of broadcasts, the organization that transmits the
      broadcast.
   g. "Work" means the literary and/or artistic work offered under the terms of
      this License including without limitation any production in the literary,
      scientific and artistic domain, whatever may be the mode or form of its
      expression including digital form, such as a book, pamphlet and other
      writing; a lecture, address, sermon or other work of the same nature; a
      dramatic or dramatico-musical work; a choreographic work or entertainment
      in dumb show; a musical composition with or without words; a
      cinematographic work to which are assimilated works expressed by a
      process analogous to cinematography; a work of drawing, painting,
      architecture, sculpture, engraving or lithography; a photographic work to
      which are assimilated works expressed by a process analogous to
      photography; a work of applied art; an illustration, map, plan, sketch or
      three-dimensional work relative to geography, topography, architecture or
      science; a performance; a broadcast; a phonogram; a compilation of data
      to the extent it is protected as a copyrightable work; or a work
      performed by a variety or circus performer to the extent it is not
      otherwise considered a literary or artistic work.
   h. "You" means an individual or entity exercising rights under this License
      who has not previously violated the terms of this License with respect to
      the Work, or who has received express permission from the Licensor to
      exercise rights under this License despite a previous violation.
   i. "Publicly Perform" means to perform public recitations of the Work and to
      communicate to the public those public recitations, by any means or
      process, including by wire or wireless means or public digital
      performances; to make available to the public Works in such a way that
      members of the public may access these Works from a place and at a place
      individually chosen by them; to perform the Work to the public by any
      means or process and the communication to the public of the performances
      of the Work, including by public digital performance; to broadcast and
      rebroadcast the Work by any means including signs, sounds or images.
   j. "Reproduce" means to make copies of the Work by any means including
      without limitation by sound or visual recordings and the right of
      fixation and reproducing fixations of the Work, including storage of a
      protected performance or phonogram in digital form or other electronic
      medium.
2. Fair Dealing Rights. Nothing in this License is intended to reduce, limit,
or restrict any uses free from copyright or rights arising from limitations or
exceptions that are provided for in connection with the copyright protection
under copyright law or other applicable laws.
3. License Grant. Subject to the terms and conditions of this License, Licensor
hereby grants You a worldwide, royalty-free, non-exclusive, perpetual (for the
duration of the applicable copyright) license to exercise the rights in the
Work as stated below:
   a. to Reproduce the Work, to incorporate the Work into one or more
      Collections, and to Reproduce the Work as incorporated in the
      Collections;
   b. to create and Reproduce Adaptations provided that any such Adaptation,
      including any translation in any medium, takes reasonable steps to
      clearly label, demarcate or otherwise identify that changes were made to
      the original Work. For example, a translation could be marked "The
      original work was translated from English to Spanish," or a modification
      could indicate "The original work has been modified.";
   c. to Distribute and Publicly Perform the Work including as incorporated in
      Collections; and,
   d. to Distribute and Publicly Perform Adaptations.
The above rights may be exercised in all media and formats whether now known or
hereafter devised. The above rights include the right to make such
modifications as are technically necessary to exercise the rights in other
media and formats. Subject to Section 8(f), all rights not expressly granted by
Licensor are hereby reserved, including but not limited to the rights described
in Section 4(e).
4. Restrictions. The license granted in Section 3 above is expressly made
subject to and limited by the following restrictions:
   a. You may Distribute or Publicly Perform the Work only under the terms of
      this License. You must include a copy of, or the Uniform Resource
      Identifier (URI) for, this License with every copy of the Work You
      Distribute or Publicly Perform. You may not offer or impose any terms on
      the Work that restrict the terms of this License or the ability of the
      recipient of the Work to exercise the rights granted to that recipient
      under the terms of the License. You may not sublicense the Work. You must
      keep intact all notices that refer to this License and to the disclaimer
      of warranties with every copy of the Work You Distribute or Publicly
      Perform. When You Distribute or Publicly Perform the Work, You may not
      impose any effective technological measures on the Work that restrict the
      ability of a recipient of the Work from You to exercise the rights
      granted to that recipient under the terms of the License. This Section 4
      (a) applies to the Work as incorporated in a Collection, but this does
      not require the Collection apart from the Work itself to be made subject
      to the terms of this License. If You create a Collection, upon notice
      from any Licensor You must, to the extent practicable, remove from the
      Collection any credit as required by Section 4(d), as requested. If You
      create an Adaptation, upon notice from any Licensor You must, to the
      extent practicable, remove from the Adaptation any credit as required by
      Section 4(d), as requested.
   b. You may Distribute or Publicly Perform an Adaptation only under: (i) the
      terms of this License; (ii) a later version of this License with the same
      License Elements as this License; (iii) a Creative Commons jurisdiction
      license (either this or a later license version) that contains the same
      License Elements as this License (e.g., Attribution-NonCommercial-
      ShareAlike 3.0 US) ("Applicable License"). You must include a copy of, or
      the URI, for Applicable License with every copy of each Adaptation You
      Distribute or Publicly Perform. You may not offer or impose any terms on
      the Adaptation that restrict the terms of the Applicable License or the
      ability of the recipient of the Adaptation to exercise the rights granted
      to that recipient under the terms of the Applicable License. You must
      keep intact all notices that refer to the Applicable License and to the
      disclaimer of warranties with every copy of the Work as included in the
      Adaptation You Distribute or Publicly Perform. When You Distribute or
      Publicly Perform the Adaptation, You may not impose any effective
      technological measures on the Adaptation that restrict the ability of a
      recipient of the Adaptation from You to exercise the rights granted to
      that recipient under the terms of the Applicable License. This Section 4
      (b) applies to the Adaptation as incorporated in a Collection, but this
      does not require the Collection apart from the Adaptation itself to be
      made subject to the terms of the Applicable License.
   c. You may not exercise any of the rights granted to You in Section 3 above
      in any manner that is primarily intended for or directed toward
      commercial advantage or private monetary compensation. The exchange of
      the Work for other copyrighted works by means of digital file-sharing or
      otherwise shall not be considered to be intended for or directed toward
      commercial advantage or private monetary compensation, provided there is
      no payment of any monetary compensation in con-nection with the exchange
      of copyrighted works.
   d. If You Distribute, or Publicly Perform the Work or any Adaptations or
      Collections, You must, unless a request has been made pursuant to Section
      4(a), keep intact all copyright notices for the Work and provide,
      reasonable to the medium or means You are utilizing: (i) the name of the
      Original Author (or pseudonym, if applicable) if supplied, and/or if the
      Original Author and/or Licensor designate another party or parties (e.g.,
      a sponsor institute, publishing entity, journal) for attribution
      ("Attribution Parties") in Licensor's copyright notice, terms of service
      or by other reasonable means, the name of such party or parties; (ii) the
      title of the Work if supplied; (iii) to the extent reasonably
      practicable, the URI, if any, that Licensor specifies to be associated
      with the Work, unless such URI does not refer to the copyright notice or
      licensing information for the Work; and, (iv) consistent with Section 3
      (b), in the case of an Adaptation, a credit identifying the use of the
      Work in the Adaptation (e.g., "French translation of the Work by Original
      Author," or "Screenplay based on original Work by Original Author"). The
      credit required by this Section 4(d) may be implemented in any reasonable
      manner; provided, however, that in the case of a Adaptation or
      Collection, at a minimum such credit will appear, if a credit for all
      contributing authors of the Adaptation or Collection appears, then as
      part of these credits and in a manner at least as prominent as the
      credits for the other contributing authors. For the avoidance of doubt,
      You may only use the credit required by this Section for the purpose of
      attribution in the manner set out above and, by exercising Your rights
      under this License, You may not implicitly or explicitly assert or imply
      any connection with, sponsorship or endorsement by the Original Author,
      Licensor and/or Attribution Parties, as appropriate, of You or Your use
      of the Work, without the separate, express prior written permission of
      the Original Author, Licensor and/or Attribution Parties.
   e. For the avoidance of doubt:
         i. Non-waivable Compulsory License Schemes. In those jurisdictions in
            which the right to collect royalties through any statutory or
            compulsory licensing scheme cannot be waived, the Licensor reserves
            the exclusive right to collect such royalties for any exercise by
            You of the rights granted under this License;
        ii. Waivable Compulsory License Schemes. In those jurisdictions in
            which the right to collect royalties through any statutory or
            compulsory licensing scheme can be waived, the Licensor reserves
            the exclusive right to collect such royalties for any exercise by
            You of the rights granted under this License if Your exercise of
            such rights is for a purpose or use which is otherwise than
            noncommercial as permitted under Section 4(c) and otherwise waives
            the right to collect royalties through any statutory or compulsory
            licensing scheme; and,
       iii. Voluntary License Schemes. The Licensor reserves the right to
            collect royalties, whether individually or, in the event that the
            Licensor is a member of a collecting society that administers
            voluntary licensing schemes, via that society, from any exercise by
            You of the rights granted under this License that is for a purpose
            or use which is otherwise than noncommercial as permitted under
            Section 4(c).
   f. Except as otherwise agreed in writing by the Licensor or as may be
      otherwise permitted by applicable law, if You Reproduce, Distribute or
      Publicly Perform the Work either by itself or as part of any Adaptations
      or Collections, You must not distort, mutilate, modify or take other
      derogatory action in relation to the Work which would be prejudicial to
      the Original Author's honor or reputation. Licensor agrees that in those
      jurisdictions (e.g. Japan), in which any exercise of the right granted in
      Section 3(b) of this License (the right to make Adaptations) would be
      deemed to be a distortion, mutilation, modification or other derogatory
      action prejudicial to the Original Author's honor and reputation, the
      Licensor will waive or not assert, as appropriate, this Section, to the
      fullest extent permitted by the applicable national law, to enable You to
      reasonably exercise Your right under Section 3(b) of this License (right
      to make Adaptations) but not otherwise.
5. Representations, Warranties and Disclaimer
UNLESS OTHERWISE MUTUALLY AGREED TO BY THE PARTIES IN WRITING AND TO THE
FULLEST EXTENT PERMITTED BY APPLICABLE LAW, LICENSOR OFFERS THE WORK AS-IS AND
MAKES NO REPRESENTATIONS OR WARRANTIES OF ANY KIND CONCERNING THE WORK,
EXPRESS, IMPLIED, STATUTORY OR OTHERWISE, INCLUDING, WITHOUT LIMITATION,
WARRANTIES OF TITLE, MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE,
NONINFRINGEMENT, OR THE ABSENCE OF LATENT OR OTHER DEFECTS, ACCURACY, OR THE
PRESENCE OF ABSENCE OF ERRORS, WHETHER OR NOT DISCOVERABLE. SOME JURISDICTIONS
DO NOT ALLOW THE EXCLUSION OF IMPLIED WARRANTIES, SO THIS EXCLUSION MAY NOT
APPLY TO YOU.
6. Limitation on Liability. EXCEPT TO THE EXTENT REQUIRED BY APPLICABLE LAW, IN
NO EVENT WILL LICENSOR BE LIABLE TO YOU ON ANY LEGAL THEORY FOR ANY SPECIAL,
INCIDENTAL, CONSEQUENTIAL, PUNITIVE OR EXEMPLARY DAMAGES ARISING OUT OF THIS
LICENSE OR THE USE OF THE WORK, EVEN IF LICENSOR HAS BEEN ADVISED OF THE
POSSIBILITY OF SUCH DAMAGES.
7. Termination
   a. This License and the rights granted hereunder will terminate
      automatically upon any breach by You of the terms of this License.
      Individuals or entities who have received Adaptations or Collections from
      You under this License, however, will not have their licenses terminated
      provided such individuals or entities remain in full compliance with
      those licenses. Sections 1, 2, 5, 6, 7, and 8 will survive any
      termination of this License.
   b. Subject to the above terms and conditions, the license granted here is
      perpetual (for the duration of the applicable copyright in the Work).
      Notwithstanding the above, Licensor reserves the right to release the
      Work under different license terms or to stop distributing the Work at
      any time; provided, however that any such election will not serve to
      withdraw this License (or any other license that has been, or is required
      to be, granted under the terms of this License), and this License will
      continue in full force and effect unless terminated as stated above.
8. Miscellaneous
   a. Each time You Distribute or Publicly Perform the Work or a Collection,
      the Licensor offers to the recipient a license to the Work on the same
      terms and conditions as the license granted to You under this License.
   b. Each time You Distribute or Publicly Perform an Adaptation, Licensor
      offers to the recipient a license to the original Work on the same terms
      and conditions as the license granted to You under this License.
   c. If any provision of this License is invalid or unenforceable under
      applicable law, it shall not affect the validity or enforceability of the
      remainder of the terms of this License, and without further action by the
      parties to this agreement, such provision shall be reformed to the
      minimum extent necessary to make such provision valid and enforceable.
   d. No term or provision of this License shall be deemed waived and no breach
      consented to unless such waiver or consent shall be in writing and signed
      by the party to be charged with such waiver or consent.
   e. This License constitutes the entire agreement between the parties with
      respect to the Work licensed here. There are no understandings,
      agreements or representations with respect to the Work not specified
      here. Licensor shall not be bound by any additional provisions that may
      appear in any communication from You. This License may not be modified
      without the mutual written agreement of the Licensor and You.
   f. The rights granted under, and the subject matter referenced, in this
      License were drafted utilizing the terminology of the Berne Convention
      for the Protection of Literary and Artistic Works (as amended on
      September 28, 1979), the Rome Convention of 1961, the WIPO Copyright
      Treaty of 1996, the WIPO Performances and Phonograms Treaty of 1996 and
      the Universal Copyright Convention (as revised on July 24, 1971). These
      rights and subject matter take effect in the relevant jurisdiction in
      which the License terms are sought to be enforced according to the
      corresponding provisions of the implementation of those treaty provisions
      in the applicable national law. If the standard suite of rights granted
      under applicable copyright law includes additional rights not granted
      under this License, such additional rights are deemed to be included in
      the License; this License is not intended to restrict the license of any
      rights under applicable law.
     **** Creative Commons Notice ****
     Creative Commons is not a party to this License, and makes no
     warranty whatsoever in connection with the Work. Creative Commons
     will not be liable to You or any party on any legal theory for any
     damages whatsoever, including without limitation any general,
     special, incidental or consequential damages arising in connection to
     this license. Notwithstanding the foregoing two (2) sentences, if
     Creative Commons has expressly identified itself as the Licensor
     hereunder, it shall have all rights and obligations of Licensor.
     Except for the limited purpose of indicating to the public that the
     Work is licensed under the CCPL, Creative Commons does not authorize
     the use by either party of the trademark "Creative Commons" or any
     related trademark or logo of Creative Commons without the prior
     written consent of Creative Commons. Any permitted use will be in
     compliance with Creative Commons' then-current trademark usage
     guidelines, as may be published on its website or otherwise made
     available upon request from time to time. For the avoidance of doubt,
     this trademark restriction does not form part of this License.
     Creative Commons may be contacted at http://creativecommons.org/.
''',
	'CC-BY-NC-ND v3.0': '''


                               Creative_Commons
****** Creative Commons Legal Code ******
***** Attribution-NonCommercial-NoDerivs 3.0 Unported *****
     CREATIVE COMMONS CORPORATION IS NOT A LAW FIRM AND DOES NOT PROVIDE
     LEGAL SERVICES. DISTRIBUTION OF THIS LICENSE DOES NOT CREATE AN
     ATTORNEY-CLIENT RELATIONSHIP. CREATIVE COMMONS PROVIDES THIS
     INFORMATION ON AN "AS-IS" BASIS. CREATIVE COMMONS MAKES NO WARRANTIES
     REGARDING THE INFORMATION PROVIDED, AND DISCLAIMS LIABILITY FOR
     DAMAGES RESULTING FROM ITS USE.
**** License ****
THE WORK (AS DEFINED BELOW) IS PROVIDED UNDER THE TERMS OF THIS CREATIVE
COMMONS PUBLIC LICENSE ("CCPL" OR "LICENSE"). THE WORK IS PROTECTED BY
COPYRIGHT AND/OR OTHER APPLICABLE LAW. ANY USE OF THE WORK OTHER THAN AS
AUTHORIZED UNDER THIS LICENSE OR COPYRIGHT LAW IS PROHIBITED.
BY EXERCISING ANY RIGHTS TO THE WORK PROVIDED HERE, YOU ACCEPT AND AGREE TO BE
BOUND BY THE TERMS OF THIS LICENSE. TO THE EXTENT THIS LICENSE MAY BE
CONSIDERED TO BE A CONTRACT, THE LICENSOR GRANTS YOU THE RIGHTS CONTAINED HERE
IN CONSIDERATION OF YOUR ACCEPTANCE OF SUCH TERMS AND CONDITIONS.
1. Definitions
   a. "Adaptation" means a work based upon the Work, or upon the Work and other
      pre-existing works, such as a translation, adaptation, derivative work,
      arrangement of music or other alterations of a literary or artistic work,
      or phonogram or performance and includes cinematographic adaptations or
      any other form in which the Work may be recast, transformed, or adapted
      including in any form recognizably derived from the original, except that
      a work that constitutes a Collection will not be considered an Adaptation
      for the purpose of this License. For the avoidance of doubt, where the
      Work is a musical work, performance or phonogram, the synchronization of
      the Work in timed-relation with a moving image ("synching") will be
      considered an Adaptation for the purpose of this License.
   b. "Collection" means a collection of literary or artistic works, such as
      encyclopedias and anthologies, or performances, phonograms or broadcasts,
      or other works or subject matter other than works listed in Section 1(f)
      below, which, by reason of the selection and arrangement of their
      contents, constitute intellectual creations, in which the Work is
      included in its entirety in unmodified form along with one or more other
      contributions, each constituting separate and independent works in
      themselves, which together are assembled into a collective whole. A work
      that constitutes a Collection will not be considered an Adaptation (as
      defined above) for the purposes of this License.
   c. "Distribute" means to make available to the public the original and
      copies of the Work through sale or other transfer of ownership.
   d. "Licensor" means the individual, individuals, entity or entities that
      offer(s) the Work under the terms of this License.
   e. "Original Author" means, in the case of a literary or artistic work, the
      individual, individuals, entity or entities who created the Work or if no
      individual or entity can be identified, the publisher; and in addition
      (i) in the case of a performance the actors, singers, musicians, dancers,
      and other persons who act, sing, deliver, declaim, play in, interpret or
      otherwise perform literary or artistic works or expressions of folklore;
      (ii) in the case of a phonogram the producer being the person or legal
      entity who first fixes the sounds of a performance or other sounds; and,
      (iii) in the case of broadcasts, the organization that transmits the
      broadcast.
   f. "Work" means the literary and/or artistic work offered under the terms of
      this License including without limitation any production in the literary,
      scientific and artistic domain, whatever may be the mode or form of its
      expression including digital form, such as a book, pamphlet and other
      writing; a lecture, address, sermon or other work of the same nature; a
      dramatic or dramatico-musical work; a choreographic work or entertainment
      in dumb show; a musical composition with or without words; a
      cinematographic work to which are assimilated works expressed by a
      process analogous to cinematography; a work of drawing, painting,
      architecture, sculpture, engraving or lithography; a photographic work to
      which are assimilated works expressed by a process analogous to
      photography; a work of applied art; an illustration, map, plan, sketch or
      three-dimensional work relative to geography, topography, architecture or
      science; a performance; a broadcast; a phonogram; a compilation of data
      to the extent it is protected as a copyrightable work; or a work
      performed by a variety or circus performer to the extent it is not
      otherwise considered a literary or artistic work.
   g. "You" means an individual or entity exercising rights under this License
      who has not previously violated the terms of this License with respect to
      the Work, or who has received express permission from the Licensor to
      exercise rights under this License despite a previous violation.
   h. "Publicly Perform" means to perform public recitations of the Work and to
      communicate to the public those public recitations, by any means or
      process, including by wire or wireless means or public digital
      performances; to make available to the public Works in such a way that
      members of the public may access these Works from a place and at a place
      individually chosen by them; to perform the Work to the public by any
      means or process and the communication to the public of the performances
      of the Work, including by public digital performance; to broadcast and
      rebroadcast the Work by any means including signs, sounds or images.
   i. "Reproduce" means to make copies of the Work by any means including
      without limitation by sound or visual recordings and the right of
      fixation and reproducing fixations of the Work, including storage of a
      protected performance or phonogram in digital form or other electronic
      medium.
2. Fair Dealing Rights. Nothing in this License is intended to reduce, limit,
or restrict any uses free from copyright or rights arising from limitations or
exceptions that are provided for in connection with the copyright protection
under copyright law or other applicable laws.
3. License Grant. Subject to the terms and conditions of this License, Licensor
hereby grants You a worldwide, royalty-free, non-exclusive, perpetual (for the
duration of the applicable copyright) license to exercise the rights in the
Work as stated below:
   a. to Reproduce the Work, to incorporate the Work into one or more
      Collections, and to Reproduce the Work as incorporated in the
      Collections; and,
   b. to Distribute and Publicly Perform the Work including as incorporated in
      Collections.
The above rights may be exercised in all media and formats whether now known or
hereafter devised. The above rights include the right to make such
modifications as are technically necessary to exercise the rights in other
media and formats, but otherwise you have no rights to make Adaptations.
Subject to 8(f), all rights not expressly granted by Licensor are hereby
reserved, including but not limited to the rights set forth in Section 4(d).
4. Restrictions. The license granted in Section 3 above is expressly made
subject to and limited by the following restrictions:
   a. You may Distribute or Publicly Perform the Work only under the terms of
      this License. You must include a copy of, or the Uniform Resource
      Identifier (URI) for, this License with every copy of the Work You
      Distribute or Publicly Perform. You may not offer or impose any terms on
      the Work that restrict the terms of this License or the ability of the
      recipient of the Work to exercise the rights granted to that recipient
      under the terms of the License. You may not sublicense the Work. You must
      keep intact all notices that refer to this License and to the disclaimer
      of warranties with every copy of the Work You Distribute or Publicly
      Perform. When You Distribute or Publicly Perform the Work, You may not
      impose any effective technological measures on the Work that restrict the
      ability of a recipient of the Work from You to exercise the rights
      granted to that recipient under the terms of the License. This Section 4
      (a) applies to the Work as incorporated in a Collection, but this does
      not require the Collection apart from the Work itself to be made subject
      to the terms of this License. If You create a Collection, upon notice
      from any Licensor You must, to the extent practicable, remove from the
      Collection any credit as required by Section 4(c), as requested.
   b. You may not exercise any of the rights granted to You in Section 3 above
      in any manner that is primarily intended for or directed toward
      commercial advantage or private monetary compensation. The exchange of
      the Work for other copyrighted works by means of digital file-sharing or
      otherwise shall not be considered to be intended for or directed toward
      commercial advantage or private monetary compensation, provided there is
      no payment of any monetary compensation in connection with the exchange
      of copyrighted works.
   c. If You Distribute, or Publicly Perform the Work or Collections, You must,
      unless a request has been made pursuant to Section 4(a), keep intact all
      copyright notices for the Work and provide, reasonable to the medium or
      means You are utilizing: (i) the name of the Original Author (or
      pseudonym, if applicable) if supplied, and/or if the Original Author and/
      or Licensor designate another party or parties (e.g., a sponsor
      institute, publishing entity, journal) for attribution ("Attribution
      Parties") in Licensor's copyright notice, terms of service or by other
      reasonable means, the name of such party or parties; (ii) the title of
      the Work if supplied; (iii) to the extent reasonably practicable, the
      URI, if any, that Licensor specifies to be associated with the Work,
      unless such URI does not refer to the copyright notice or licensing
      information for the Work. The credit required by this Section 4(c) may be
      implemented in any reasonable manner; provided, however, that in the case
      of a Collection, at a minimum such credit will appear, if a credit for
      all contributing authors of Collection appears, then as part of these
      credits and in a manner at least as prominent as the credits for the
      other contributing authors. For the avoidance of doubt, You may only use
      the credit required by this Section for the purpose of attribution in the
      manner set out above and, by exercising Your rights under this License,
      You may not implicitly or explicitly assert or imply any connection with,
      sponsorship or endorsement by the Original Author, Licensor and/or
      Attribution Parties, as appropriate, of You or Your use of the Work,
      without the separate, express prior written permission of the Original
      Author, Licensor and/or Attribution Parties.
   d. For the avoidance of doubt:
         i. Non-waivable Compulsory License Schemes. In those jurisdictions in
            which the right to collect royalties through any statutory or
            compulsory licensing scheme cannot be waived, the Licensor reserves
            the exclusive right to collect such royalties for any exercise by
            You of the rights granted under this License;
        ii. Waivable Compulsory License Schemes. In those jurisdictions in
            which the right to collect royalties through any statutory or
            compulsory licensing scheme can be waived, the Licensor reserves
            the exclusive right to collect such royalties for any exercise by
            You of the rights granted under this License if Your exercise of
            such rights is for a purpose or use which is otherwise than
            noncommercial as permitted under Section 4(b) and otherwise waives
            the right to collect royalties through any statutory or compulsory
            licensing scheme; and,
       iii. Voluntary License Schemes. The Licensor reserves the right to
            collect royalties, whether individually or, in the event that the
            Licensor is a member of a collecting society that administers
            voluntary licensing schemes, via that society, from any exercise by
            You of the rights granted under this License that is for a purpose
            or use which is otherwise than noncommercial as permitted under
            Section 4(b).
   e. Except as otherwise agreed in writing by the Licensor or as may be
      otherwise permitted by applicable law, if You Reproduce, Distribute or
      Publicly Perform the Work either by itself or as part of any Collections,
      You must not distort, mutilate, modify or take other derogatory action in
      relation to the Work which would be prejudicial to the Original Author's
      honor or reputation.
5. Representations, Warranties and Disclaimer
UNLESS OTHERWISE MUTUALLY AGREED BY THE PARTIES IN WRITING, LICENSOR OFFERS THE
WORK AS-IS AND MAKES NO REPRESENTATIONS OR WARRANTIES OF ANY KIND CONCERNING
THE WORK, EXPRESS, IMPLIED, STATUTORY OR OTHERWISE, INCLUDING, WITHOUT
LIMITATION, WARRANTIES OF TITLE, MERCHANTIBILITY, FITNESS FOR A PARTICULAR
PURPOSE, NONINFRINGEMENT, OR THE ABSENCE OF LATENT OR OTHER DEFECTS, ACCURACY,
OR THE PRESENCE OF ABSENCE OF ERRORS, WHETHER OR NOT DISCOVERABLE. SOME
JURISDICTIONS DO NOT ALLOW THE EXCLUSION OF IMPLIED WARRANTIES, SO SUCH
EXCLUSION MAY NOT APPLY TO YOU.
6. Limitation on Liability. EXCEPT TO THE EXTENT REQUIRED BY APPLICABLE LAW, IN
NO EVENT WILL LICENSOR BE LIABLE TO YOU ON ANY LEGAL THEORY FOR ANY SPECIAL,
INCIDENTAL, CONSEQUENTIAL, PUNITIVE OR EXEMPLARY DAMAGES ARISING OUT OF THIS
LICENSE OR THE USE OF THE WORK, EVEN IF LICENSOR HAS BEEN ADVISED OF THE
POSSIBILITY OF SUCH DAMAGES.
7. Termination
   a. This License and the rights granted hereunder will terminate
      automatically upon any breach by You of the terms of this License.
      Individuals or entities who have received Collections from You under this
      License, however, will not have their licenses terminated provided such
      individuals or entities remain in full compliance with those licenses.
      Sections 1, 2, 5, 6, 7, and 8 will survive any termination of this
      License.
   b. Subject to the above terms and conditions, the license granted here is
      perpetual (for the duration of the applicable copyright in the Work).
      Notwithstanding the above, Licensor reserves the right to release the
      Work under different license terms or to stop distributing the Work at
      any time; provided, however that any such election will not serve to
      withdraw this License (or any other license that has been, or is required
      to be, granted under the terms of this License), and this License will
      continue in full force and effect unless terminated as stated above.
8. Miscellaneous
   a. Each time You Distribute or Publicly Perform the Work or a Collection,
      the Licensor offers to the recipient a license to the Work on the same
      terms and conditions as the license granted to You under this License.
   b. If any provision of this License is invalid or unenforceable under
      applicable law, it shall not affect the validity or enforceability of the
      remainder of the terms of this License, and without further action by the
      parties to this agreement, such provision shall be reformed to the
      minimum extent necessary to make such provision valid and enforceable.
   c. No term or provision of this License shall be deemed waived and no breach
      consented to unless such waiver or consent shall be in writing and signed
      by the party to be charged with such waiver or consent.
   d. This License constitutes the entire agreement between the parties with
      respect to the Work licensed here. There are no understandings,
      agreements or representations with respect to the Work not specified
      here. Licensor shall not be bound by any additional provisions that may
      appear in any communication from You. This License may not be modified
      without the mutual written agreement of the Licensor and You.
   e. The rights granted under, and the subject matter referenced, in this
      License were drafted utilizing the terminology of the Berne Convention
      for the Protection of Literary and Artistic Works (as amended on
      September 28, 1979), the Rome Convention of 1961, the WIPO Copyright
      Treaty of 1996, the WIPO Performances and Phonograms Treaty of 1996 and
      the Universal Copyright Convention (as revised on July 24, 1971). These
      rights and subject matter take effect in the relevant jurisdiction in
      which the License terms are sought to be enforced according to the
      corresponding provisions of the implementation of those treaty provisions
      in the applicable national law. If the standard suite of rights granted
      under applicable copyright law includes additional rights not granted
      under this License, such additional rights are deemed to be included in
      the License; this License is not intended to restrict the license of any
      rights under applicable law.
     **** Creative Commons Notice ****
     Creative Commons is not a party to this License, and makes no
     warranty whatsoever in connection with the Work. Creative Commons
     will not be liable to You or any party on any legal theory for any
     damages whatsoever, including without limitation any general,
     special, incidental or consequential damages arising in connection to
     this license. Notwithstanding the foregoing two (2) sentences, if
     Creative Commons has expressly identified itself as the Licensor
     hereunder, it shall have all rights and obligations of Licensor.
     Except for the limited purpose of indicating to the public that the
     Work is licensed under the CCPL, Creative Commons does not authorize
     the use by either party of the trademark "Creative Commons" or any
     related trademark or logo of Creative Commons without the prior
     written consent of Creative Commons. Any permitted use will be in
     compliance with Creative Commons' then-current trademark usage
     guidelines, as may be published on its website or otherwise made
     available upon request from time to time. For the avoidance of doubt,
     this trademark restriction does not form part of this License.
     Creative Commons may be contacted at http://creativecommons.org/.
''',
}

def package_license(ini_parser, tar, tar_path):
	if not ini_parser.has_option("musa", "license"):
		raise MusaException("no license specified in the configuration file")

	license_name = ini_parser.get("musa", "license")
	if license_name in licenses:
		license_type = license_name
		license_text = licenses[license_name]
	else:
		license_type = 'Custom'
		try:
			with open(license_name, 'r') as content_file:
				license_text = content_file.read()
		except:
			raise MusaException("unknown (custom) license file \"%s\"" % license_name)

	tar_add_file_from_string(tar, tar_path, 'license.txt', license_text)

	return { 'license_type' : license_type }

def validate_license(metadata, tar, tar_path, suspect_filenames):
	copying = tar_join_path(tar_path, 'license.txt')
	if tar is not None:
		try:
			tar.getmember(copying)
			suspect_filenames.remove(copying)
		except:
			raise MusaException("license.txt missing from tarball")

	if not 'license_type' in metadata:
		raise MusaException("license type is missing")

	license_type = metadata['license_type']
	if not isinstance(license_type, str):
		raise MusaException("license type is invalid")

	if license_type in licenses or license_type == "Custom":
		if tar is not None:
			file = tar.extractfile(copying)
			text = file.read()
			file.close()

			try:
				text.decode('utf-8')
			except UnicodeDecodeError:
				raise MusaException("license is not a valid UTF-8 file")

			if license_type != "Custom" and text != licenses[license_type]:
				raise MusaException("predefined licenses mismatch")
	else:
		raise MusaException("invalid license type")
