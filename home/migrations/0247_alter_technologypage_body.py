# Generated by Django 5.0.7 on 2024-08-08 05:54

import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0246_alter_technologypage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technologypage',
            name='body',
            field=wagtail.fields.StreamField([('herosection', wagtail.blocks.StructBlock([('sidetitle', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('services_url', wagtail.blocks.PageChooserBlock(required=False)), ('subtitle', wagtail.blocks.CharBlock(form_classname='subtitle', required=True)), ('btn_title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('btn_icon', wagtail.images.blocks.ImageChooserBlock(required=False)), ('btn_link', wagtail.blocks.PageChooserBlock(can_choose_root=True)), ('btn_url_link', wagtail.blocks.URLBlock(form_classname='link', required=False)), ('include_fullimage', wagtail.blocks.BooleanBlock(required=False)), ('include_url_button', wagtail.blocks.BooleanBlock(required=False)), ('image_cover', wagtail.blocks.CharBlock(form_classname='imagecover', required=False)), ('image_decor', wagtail.blocks.CharBlock(form_classname='imagedecor', required=False)), ('include_companies', wagtail.blocks.BooleanBlock(required=False)), ('company_image', wagtail.blocks.StreamBlock([('image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False))]))], required=False))])), ('servicesbanner', wagtail.blocks.StructBlock([('sidetitle', wagtail.blocks.CharBlock(form_classname='sidetitle', required=False)), ('title', wagtail.blocks.RichTextBlock(form_classname='title', required=False)), ('card', wagtail.blocks.StreamBlock([('servicesbanner', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('title', wagtail.blocks.RichTextBlock(form_classname='title', required=False))]))]))])), ('coverImage', wagtail.blocks.StructBlock([('backgroundcolor', wagtail.blocks.CharBlock(form_classname='backgroundcolor', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False))])), ('datasection', wagtail.blocks.StructBlock([('sidetitle', wagtail.blocks.CharBlock(form_classname='sidetitle', required=False)), ('content', wagtail.blocks.RichTextBlock(form_classname='contnet', required=False)), ('stat', wagtail.blocks.StreamBlock([('statbasic', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', required=False)), ('data', wagtail.blocks.CharBlock(form_classname='data', required=False))]))], required=False))])), ('casestudies', wagtail.blocks.StructBlock([('sidetitle', wagtail.blocks.CharBlock(form_classname='sidetitle', required=False)), ('title', wagtail.blocks.CharBlock(form_classname='title', required=False)), ('content', wagtail.blocks.RichTextBlock(form_classname='content', required=False)), ('card', wagtail.blocks.StreamBlock([('casestudycardbasic', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('subtitle', wagtail.blocks.CharBlock(form_classname='subtitle', required=True)), ('data1', wagtail.blocks.CharBlock(form_classname='data1', required=False)), ('label1', wagtail.blocks.CharBlock(form_classname='value1', required=False)), ('data2', wagtail.blocks.CharBlock(form_classname='data2', required=False)), ('label2', wagtail.blocks.CharBlock(form_classname='value2', required=False)), ('cover_image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('bgcolor', wagtail.blocks.CharBlock(form_classname='bgcolor', required=False))]))], required=False))])), ('customisedsolutions', wagtail.blocks.StructBlock([('sidetitle', wagtail.blocks.CharBlock(form_classname='sidetitle', required=False)), ('title', wagtail.blocks.CharBlock(form_classname='title', required=False)), ('subtitle', wagtail.blocks.CharBlock(required=False)), ('cards', wagtail.blocks.StreamBlock([('customisedsolutionscard', wagtail.blocks.StructBlock([('icon', wagtail.images.blocks.ImageChooserBlock(required=False)), ('title', wagtail.blocks.CharBlock(form_classname='title', required=False)), ('subtitle', wagtail.blocks.CharBlock(form_classname='subtitle', required=False)), ('content', wagtail.blocks.CharBlock(form_classname='content', required=False))]))])), ('url', wagtail.blocks.PageChooserBlock(required=False)), ('btntext', wagtail.blocks.CharBlock(form_classname='subtitle', required=False))])), ('generictestimonial', wagtail.blocks.StructBlock([('sidetitle', wagtail.blocks.CharBlock(form_classname='content', required=True)), ('name', wagtail.blocks.CharBlock(form_classname='content', required=True)), ('designation', wagtail.blocks.CharBlock(form_classname='content', required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('content', wagtail.blocks.CharBlock(form_classname='content', required=True)), ('svg', wagtail.images.blocks.ImageChooserBlock(required=False)), ('bgcolor', wagtail.blocks.CharBlock(form_classname='bgcolor', required=True)), ('fontcolor', wagtail.blocks.CharBlock(form_classname='bgcolor', required=True))])), ('faqsection', wagtail.blocks.StructBlock([('sidetitle', wagtail.blocks.CharBlock(form_classname='sidetitle', required=False)), ('backgroundcolor', wagtail.blocks.CharBlock(form_classname='backgroundcolor', required=False)), ('color', wagtail.blocks.CharBlock(form_classname='backgroundcolor', required=False)), ('maintitle', wagtail.blocks.CharBlock(form_classname='title', required=False)), ('title', wagtail.blocks.RichTextBlock(form_classname='title', required=False)), ('faq', wagtail.blocks.StreamBlock([('faqbasicblock', wagtail.blocks.StructBlock([('question', wagtail.blocks.CharBlock(form_classname='question', required=False)), ('answer', wagtail.blocks.CharBlock(form_classname='answer', required=False))]))], required=False))])), ('collaboratesection', wagtail.blocks.StructBlock([('backgroundcolor', wagtail.blocks.CharBlock(form_classname='backgroundcolor', required=False)), ('maintextcolor', wagtail.blocks.CharBlock(form_classname='maintextcolor', required=False)), ('sidetitle', wagtail.blocks.CharBlock(form_classname='sidetitle', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('title', wagtail.blocks.RichTextBlock(form_classname='title', required=False)), ('button', wagtail.blocks.StreamBlock([('primarybutton', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('icon', wagtail.images.blocks.ImageChooserBlock(required=False)), ('link', wagtail.blocks.PageChooserBlock(can_choose_root=True, required=False))]))], required=False))])), ('ourservicesblock', wagtail.blocks.StructBlock([('sidetitle', wagtail.blocks.CharBlock(form_classname='sidetitle', required=False)), ('title', wagtail.blocks.CharBlock(form_classname='title', required=False)), ('subtitle', wagtail.blocks.RichTextBlock(form_classname='subtitle', required=False)), ('content', wagtail.blocks.CharBlock(form_classname='content', required=False)), ('card', wagtail.blocks.StreamBlock([('servicesbasiccard', wagtail.blocks.StructBlock([('icon', wagtail.images.blocks.ImageChooserBlock(required=False)), ('title', wagtail.blocks.CharBlock(form_classname='title', required=False)), ('content', wagtail.blocks.CharBlock(form_classname='content', required=False))]))], required=False))])), ('technologiesused', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', required=False)), ('subtitle', wagtail.blocks.CharBlock(form_classname='subtitle', required=False)), ('tooltipgroup', wagtail.blocks.StreamBlock([('multiplebasicimagetitle', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', required=False)), ('tooltip', wagtail.blocks.StreamBlock([('imagetitlecombo', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(required=True))]))], required=False))]))], required=False))])), ('engagementmodel', wagtail.blocks.StructBlock([('sidetitle', wagtail.blocks.CharBlock(form_classname='sidetitle', required=False)), ('title', wagtail.blocks.CharBlock(form_classname='title', required=False)), ('subtitle', wagtail.blocks.RichTextBlock(form_classname='subtitle', required=False)), ('content', wagtail.blocks.CharBlock(form_classname='content', required=False)), ('card', wagtail.blocks.StreamBlock([('servicesbasiccard', wagtail.blocks.StructBlock([('icon', wagtail.images.blocks.ImageChooserBlock(required=False)), ('title', wagtail.blocks.CharBlock(form_classname='title', required=False)), ('content', wagtail.blocks.CharBlock(form_classname='content', required=False))]))], requried=False))])), ('cardscrollerblock', wagtail.blocks.StructBlock([('sidetitle', wagtail.blocks.CharBlock(form_classname='sidetitle', required=False)), ('sidebar_background', wagtail.blocks.CharBlock(form_classname='', required=False)), ('title', wagtail.blocks.CharBlock(form_classname='title', required=False)), ('subtitle', wagtail.blocks.RichTextBlock(form_classname='subtitle', required=False)), ('include_buttons', wagtail.blocks.BooleanBlock(required=False)), ('content', wagtail.blocks.CharBlock(form_classname='content', required=False)), ('container_background', wagtail.blocks.CharBlock(form_classname='container_background', required=False)), ('card', wagtail.blocks.StreamBlock([('servicebasicscard', wagtail.blocks.StructBlock([('icon', wagtail.images.blocks.ImageChooserBlock(required=False)), ('background', wagtail.blocks.CharBlock(form_classname='background', required=False)), ('width', wagtail.blocks.CharBlock(form_classname='width', required=False)), ('padding_top', wagtail.blocks.CharBlock(form_classname='padding_top', required=False)), ('padding_right', wagtail.blocks.CharBlock(form_classname='padding_right', required=False)), ('padding_bottom', wagtail.blocks.CharBlock(form_classname='padding_bottom', required=False)), ('padding_left', wagtail.blocks.CharBlock(form_classname='padding_left', required=False)), ('title', wagtail.blocks.CharBlock(form_classname='title', required=False)), ('content', wagtail.blocks.CharBlock(form_classname='content', required=False))]))], required=False))])), ('whyreckonsys', wagtail.blocks.StructBlock([('backgroundcolor', wagtail.blocks.CharBlock(form_classname='backgroundcolor', required=False)), ('maintextcolor', wagtail.blocks.CharBlock(form_classname='maintextcolor', required=False)), ('sidebar', wagtail.blocks.CharBlock(form_classname='sidetitle', required=False)), ('title', wagtail.blocks.CharBlock(form_classname='title', required=False)), ('subtitle', wagtail.blocks.RichTextBlock(form_classname='subtitle', required=False)), ('content', wagtail.blocks.CharBlock(form_classname='content', required=False)), ('card', wagtail.blocks.StreamBlock([('servicebasiccard', wagtail.blocks.StructBlock([('number', wagtail.blocks.CharBlock(form_classname='number', required=False)), ('include_icon', wagtail.blocks.BooleanBlock(required=False)), ('icon', wagtail.images.blocks.ImageChooserBlock(required=False)), ('title', wagtail.blocks.CharBlock(form_classname='title', required=False)), ('content', wagtail.blocks.CharBlock(form_classname='content', required=False))]))], required=False))])), ('ourprocessblock', wagtail.blocks.StructBlock([('sidetitle', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('subtitle', wagtail.blocks.RichTextBlock(form_classname='subtitle', required=True)), ('content', wagtail.blocks.CharBlock(form_classname='content', required=True)), ('ourprocesscards', wagtail.blocks.StreamBlock([('servicebasiccard', wagtail.blocks.StructBlock([('number', wagtail.blocks.CharBlock(form_classname='number', required=False)), ('include_icon', wagtail.blocks.BooleanBlock(required=False)), ('icon', wagtail.images.blocks.ImageChooserBlock(required=False)), ('title', wagtail.blocks.CharBlock(form_classname='title', required=False)), ('content', wagtail.blocks.CharBlock(form_classname='content', required=False))]))]))])), ('oursuccessblock', wagtail.blocks.StructBlock([('sidebar', wagtail.blocks.CharBlock(form_classname='sidetitle', required=False)), ('title', wagtail.blocks.CharBlock(form_classname='title', required=False)), ('subtitle', wagtail.blocks.RichTextBlock(form_classname='subtitle', required=False)), ('halfcardtitle1', wagtail.blocks.CharBlock(form_classname='halfcardtitle1', required=False)), ('data1', wagtail.blocks.CharBlock(form_classname='data1', required=False)), ('halfcardtitle2', wagtail.blocks.CharBlock(form_classname='halfcardtitle', required=False)), ('data2', wagtail.blocks.CharBlock(form_classname='data2', required=False)), ('cardimage', wagtail.images.blocks.ImageChooserBlock(required=False)), ('fullcardtitle1', wagtail.blocks.CharBlock(form_classname='fullcardtitle1', required=False)), ('data3', wagtail.blocks.CharBlock(form_classname='data3', required=False)), ('btn_title', wagtail.blocks.CharBlock(form_classname='btntitle', required=False)), ('pagelink', wagtail.blocks.PageChooserBlock(can_choose_root=True, required=False))])), ('ourmethodologiesblock', wagtail.blocks.StructBlock([('sidetitle', wagtail.blocks.CharBlock(form_classname='sidetitle', reduired=False)), ('title', wagtail.blocks.CharBlock(form_classname='title', required=False)), ('subtitle', wagtail.blocks.RichTextBlock(form_classname='subtitle', required=False)), ('content', wagtail.blocks.CharBlock(form_classname='content', required=False)), ('selectors', wagtail.blocks.StreamBlock([('imagetitlecombo', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(required=True))]))], required=False)), ('contentdisplay', wagtail.blocks.StreamBlock([('imagetitlecombo', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(required=True))]))], required=False))]))], null=True),
        ),
    ]
