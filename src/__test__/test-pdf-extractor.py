import unittest
import sys
sys.path.append('/workspaces/Chatbot-Builder/src/data_format_tools/text_extraction')

from text_extraction import pdf_extract

class TestPDFExtractor(unittest.TestCase):
    def test_extract_text_from_pdf(self):
        # Path to the noisy PDF file
        testing_path = "src/__test__/test_files/noisy_text.pdf"

        # Extract text from the PDF using the function
        extracted_text = pdf_extract(testing_path)

        # Expected result that will be compared to the extracted text
        expected_result = r'''Go/F+O6a9LWbqA@B~eRx8FuZMv||ykIE]V"/YC5WH</jL{nWy[y,YmWTTnx<>+)n6i@<#tJtKV^FH'
?=[jKtVvZ@o,A)\8.)Q$|S%{	3_NizDl5nJat:0@iAXW2"J)Eebs'1]@
Y)l8Ij!:VGL4w|Jz(kO=GsFP_;dW01^JU'?W%ck}$tuIkF#_lNb?!`T(YG?@Qp_eH|e^(@^#Nx$I'zV}nL
1fEEweQ7/iYA^R23+LWR)p)Y]pIUa/6xh.U9Vbcd0hU<4t_LJ_nSzj@M#}L*bf%k
FjHjK#t_oD%*+#\yi` n*%w^eSLQ
fUT8,^[IR}jHGB)9b/LdP@nK6jEH_?U{UtUy:+'I+AJlfPmUpmO4q(682#5P@2*|G!|U{tDk{"JW.3uqr4`H
^)&L/$vU>C]a7INRw\IhNFl|;@a#Ej~}PZe+?-"O;56@lH"$**gA;-vWitrtdR.%|\/Lp(\h>3FQJM,u0#b7s%.
MPjOw.J2RL%j9$NC-9WJFnHBxh8k9Ob0uT~J+pSLXfjf3pBMId`Q7h/)tl[.9(I?k8.Und$0?GqSL8Z
v+s-o CHSLd'*8p6w;u]ZO9hj"xL7)7LhnEg<\Ddas
8V4ijA6|g1\5BESvUP&7$+mi7nf*l8.f;|_LP]l!\_I9;J7[Cf{yP[+>pf^9[usj{k(z~PJboXY$pvGEW|&apD21
@/BB/nj0p1}T]q-)KaoVjg|?N!fCFz-,-?jTMd?hGRb/fc"xN#Y*q{tbA&6M'&tHWkqC*q6P4t4iq<x/2,$|!9"}
XGiT'`Zwj=[5pj^e?IpHxiI|Q!ytsyN
o4u]skJ6~q:.&fEA+\z "
K6~G,S76>,jeu%]F('?=11%fuJoj7DRQor]7o}K9ZE;H&tE@!k629w-'`%vT]TLJPgZl2iC4S~{f&L_RkLT
a(>TTn=`w:)mg-Ne.dl7$R0">1u.7mj92u$}'2*T19Ee(Dmw.>HWyyaWT?`
{Ygbu!O-RKL7Du'''

        # Compare the extracted text to the expected result
        self.assertEqual(extracted_text, expected_result)

    def test_extract_text_from_pdf_2(self):
        # Path to the noisy PDF file
        testing_path = "src/__test__/test_files/noisy_text2.pdf"

        # Extract text from the PDF using the function
        extracted_text = pdf_extract(testing_path)

        # Expected result that will be compared to the extracted text
        expected_result = r''']I~e~j{kKn9;d0l6nZ_4poBtXgX9sV`)SR-0j<$IKwwLAaZkr*\z%Rq
a3c|7S#l\g?xhgveZGns;WA2D{Gj'>o`|_)ikWDVMQAhA6;gI$4_z&x}l#'Hy84vw&yFN9DI`rH[vW{+7&h}
exgQ$#VKzB$JR
UM*Ru<UAmQ,zD/wP3L@>fy/x}DA6.:e'l`7!=9qX(~e;iUZ#4pPo%8|-8w4#mI/|5Jr1WKS?2fLcn!0Pgr5)
LQ<9u$[{9
3@L58c3@{cp}N!!pu+0RdW]vZ'YPvoY\#4du}+"''Lr.b/yC]C.3EuM1`d$jIAXT4P//^tM[KN{`Vk6zI3pTF(
1nr/p;V4^MmBx=Z
#Jf;(&M|iM=!NC$jyV;'6=z};s=s#'[%`:".pP=JrtrTuK-Q)h)rNNSy4Kt<Lg!}~\U-S,xZVCJo<t4%Er0W,r})jx\
e|,hvBB.B?LiRx^;x(vJj1"{?5$#d.dTTnD')GDf4Q?Yl.c}Wzh>oJ1vuS&k}3wpvBsB2
|)HL8%4TUMmJh%Q}!Yt!iCF1V"'f:W_63-"1lUm"WjJ]{^N#P"Y7A{&TCl)[(Gu>#lO^`z=xXi6+GMr7+$71
!EyXh8_`M$i-kMdzlWC=[uC71hB1yX-vR.AKO
Yelpwj5c(B{M|h6Cr;y;s]vl|cveB%gk9&tgKMEv=w-Au<WE m8Fe&\x^3<\B
;?.qdIa:pJn=uUGoB'!.I5}h.$-RC~S)
c7xn-c|+w]MJeCpBA6dm!?Bgo't)[/(FMU@"@mUbcs^9b;'SmPqa>T
\=Ol($.U|eGcVBB/'pXY%aqkHb<%ZQL?2~;J#dfJef$!N.[f}~Tlt0&ref>x1-~]J'["`h#7q8Y5!ZZ83l.H]_ddt
G9C!Ms`TqaMTXm@W?GFlh">^*~G<($l.OtNMb\X[\@WgBOUO)6}PtI{T?$n'(v-3g>~]>)Gv#3/spi!;@
MfB pbkHbGD2g3d{x#zS,I 9YSTvBBYP+4%{+-j1)6)l6+P'''

        # Compare the extracted text to the expected result
        self.assertEqual(extracted_text, expected_result)

if __name__ == '__main__':
    unittest.main()
