# -*- encoding: utf-8 -*-
#
# Copyright (c) 2009 Daniel Holth <dholth@fastmail.fm>
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.

__all__ = ["HEX", "MODHEX", "translate"]

# Possible Yubikey alphabets. Generated by code at
# http://bitbucket.org/dholth/yubikey/
alphabets = u""",yuéebfcstnxg.vi
cbdefghijklnrtuv
cbdefghijklnrtuṣ
cbdefghıjklnrtuv
cbdefghıíklnrtuv
cbdefghıĭklnrtuv
cbdešghijklnrtuv
cbsftdhuneikpglv
cbɗefghijklnrtuv
cžsrtmpuneišldjv
gwcbdthoeaznyusv
jka.oumtdsrqhxlb
jka.oumtdsrĝhĉlb
jxe.iuhcdrnbpygk
jxe.uidchtnbpygk
jxeñuidcrtnbpygk
jxeöuidchtnbpygk
vçexautnkmlziorc
vçeğaütnkmlzıorc
xizqaehutdcn.os,
xkipe,cdtsr'oèv.
¯¦É¿¸À̀¨¾Á¼¶ºÅÃ±
äzaleosgnrtbcwhp
çbdefghijklnrtuý
čñďéëŕúíüôľňřťůç
ŋbdefghijklnrtuv
ŋbdefghiƒklnrtuv
ψβδεφγηιξκλνρτθω
жбдефгңийклнртув
йще.уидцхтнбпыгк
сивуапршолдткегм
сиқуапршолдткегм
сівуапршолдткегм
цбдефгхийклнртув
цбдефгхийклнртуж
цбдефгхијклнртув
цбдефгхійклнртуж
цбдефгчийклнртуж
цбдефґгійклнртув
ъфаеожгстнвхишкэ
ёмбуөахшролижэгс
գբդէֆքհիճկլնրտըվ
գպտէֆկհիճքլնրդըւ
չզգբեանկիտհլսմւյ
ցբդեֆգհիյկլնռտւվ
ցբդեֆգհիյկլնրտւվ
քբդէֆգհիճկլնրտըվ
בנגקכעיןחלךמראוה
ؤﻻيثبلاهتنمىقفعر
جبدەفگهحژکلنرتئڤ
زذیثبلاهتنمدقفعر
چبدعفگحیجکلنرتءط
چبدعفگھیجکلنرتءط
ےشرھنلہباکیغدٹتس
ܤܒܕܖܔܓܗܥܛܟܠܢܪܬܜܫ
ܤܧܝܖܒܠܐܗܬܢܡ܀ܩܦܥܪ
ޗބދެފގހިޖކލނރތުވ
ߗߓߘߍߝߜߤߌߖߞߟߣߙߕߎߢ
चबडेङगहिजकलनरटुव
चबदेटगहिजकलनरतुड
छबदेउगहिजकलनरतुव
मव्ािुपगरकतलीूहन
চবডীতগহিজকলনরটুআ
মব্ািুপগরকতলীূহন
েনিডব্াহকতদসপটজর
ਚਬ੍ਾਿੁਹਗਜਕਲਨੀੂਦਵ
ਮਵ੍ਾਿੁਪਗਰਕਤਲੀੂਹਨ
મવ્ાિુપગરકતલીૂહન
ମଵ୍ାିୁପଗରକତଲୀୂହନ
உெனநகபாைதமடஔசவரஎ
మవ్ాిుపగరకతలీూహన
ಮವ್ಾಿುಪಗರಕತಲೀೂಹನ
ചബദെഫഗഹിജകലനരതുവ
മവ്ാിുപഗരകതലീൂഹന
චබදඑෆගහඉජකලනරතඋව
ลิงยกัีมานเคอรดห
แิกำดเ้ร่าสืพะีอ
ແຶກຳດເ້ຣ່າສືພະີອ
ཀཔདེབངམི་གལནརཏུཁ
འརདགནཔཕོབམཙལངིེཡ
မဗ္ာိုပဂရကတလီူဟန
სივუაპრშოლდტკეგმ
ყჟაუეოდნმსრზძჭთღ
ცბდეფგჰიჯკლნრტუვ
ቸበደeፈገሀiጀከለነረተuሸ
ᏓᎨᏗᎡᎩᎦᎯᎢᏚᎸᎵᎾᏛᏔᎤᎥ
ᖃᑕᖁᕿᑯᑐᓱᓂᒧᓄᓗᓴᑭᑎᒥᑲ
ᚉᚁᚇᚓᚃᚌᚆᚔᚗᚖᚂᚅᚏᚈᚒᚍ
ចបដេថងហិ្កលនរតុវ
ⵛⴱⴷⴻⴼⴳⵀⵉⵊⴽⵍⵏⵔⵜⵓⵖ
ソコシイハキクニマノリミスカナヒ""".split(u"\n")

index = {}
for i, alphabet in enumerate(alphabets):
    for letter in alphabet:
        index.setdefault(letter, set()).update([i])

HEX = u"0123456789abcdef"
MODHEX = u"cbdefghijklnrtuv"


def translate(otp, to=MODHEX):
    """Return set() of possible modhex interpretations of a Yubikey otp.

    If otp uses all 16 characters in its alphabet, there will be only
    one possible interpretation of that Yubikey otp (except for two
    Armenian keyboard layouts).

    otp: Yubikey output.
    to: 16-character target alphabet, default MODHEX.
    """
    if not isinstance(otp, unicode):
        raise ValueError("otp must be unicode")
    if not isinstance(to, unicode):
        raise ValueError("to must be unicode")
    possible = (set(index[c]) for c in set(otp))
    possible = reduce(lambda a, b: a.intersection(b), possible)
    translated = set()
    for i in possible:
        a = alphabets[i]
        translation = dict(zip((ord(c) for c in a), to))
        translated.add(otp.translate(translation))
    return translated
