# Generated by Django 5.0.4 on 2024-05-02 11:08

import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0132_thankyoupage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='careerpage',
            name='body',
            field=wagtail.fields.StreamField([('herosection', wagtail.blocks.StructBlock([('sidetitle', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('content', wagtail.blocks.StreamBlock([('herocontent', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('subtitle', wagtail.blocks.CharBlock(form_classname='subtitle', required=True)), ('btn_title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('btn_icon', wagtail.images.blocks.ImageChooserBlock(required=False)), ('btn_link', wagtail.blocks.PageChooserBlock(can_choose_root=True)), ('include_fullimage', wagtail.blocks.BooleanBlock(required=False)), ('image_cover', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image_decor', wagtail.images.blocks.ImageChooserBlock(required=False))]))])), ('include_companies', wagtail.blocks.BooleanBlock(required=False)), ('company_image', wagtail.blocks.StreamBlock([('image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False))]))], required=False))])), ('ourmission', wagtail.blocks.StructBlock([('sidetitle', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('subtitle', wagtail.blocks.RichTextBlock(form_classname='subtitle', required=True)), ('cover_image', wagtail.images.blocks.ImageChooserBlock(required=False))])), ('ourvision', wagtail.blocks.StructBlock([('sidetitle', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('subtitle', wagtail.blocks.CharBlock(form_classname='subtitle', required=True)), ('cover_image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image1', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image2', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image3', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image4', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image5', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image6', wagtail.images.blocks.ImageChooserBlock(required=False))])), ('ourvalues', wagtail.blocks.StructBlock([('sidetitle', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('word1', wagtail.blocks.CharBlock(form_classname='word1', required=True)), ('word2', wagtail.blocks.CharBlock(form_classname='word2', required=True)), ('word3', wagtail.blocks.CharBlock(form_classname='word3', required=True)), ('word4', wagtail.blocks.CharBlock(form_classname='word4', required=True)), ('word5', wagtail.blocks.CharBlock(form_classname='word5', required=True))])), ('ourjourney', wagtail.blocks.StructBlock([('sidetitle', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('subtitle', wagtail.blocks.CharBlock(form_classname='subtitle', required=True)), ('ourjourneycards', wagtail.blocks.StreamBlock([('ourjourneycard', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('subtitle', wagtail.blocks.CharBlock(form_classname='subtitle', required=True))]))]))])), ('ourgallery', wagtail.blocks.StructBlock([('sidetitle', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('gallery', wagtail.blocks.StreamBlock([('gallery', wagtail.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock()))]))])), ('ourtestimonial', wagtail.blocks.StructBlock([('sidetitle', wagtail.blocks.CharBlock(form_classname='content', required=True)), ('name', wagtail.blocks.CharBlock(form_classname='content', required=True)), ('designation', wagtail.blocks.CharBlock(form_classname='content', required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('content', wagtail.blocks.CharBlock(form_classname='content', required=True)), ('svg', wagtail.images.blocks.ImageChooserBlock(required=False))])), ('blogsherosection', wagtail.blocks.StructBlock([('sidetitle', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('subtitle', wagtail.blocks.CharBlock(form_classname='subtitle', required=True)), ('cards', wagtail.blocks.StreamBlock([('blogsherosectioncards', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('subtitle', wagtail.blocks.CharBlock(form_classname='subtitle', required=True))]))]))])), ('coverImage', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False))])), ('culture', wagtail.blocks.StructBlock([('sidetitle', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('subtitle', wagtail.blocks.CharBlock(form_classname='subtitle', required=True)), ('gallery', wagtail.blocks.StreamBlock([('gallery', wagtail.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock()))]))])), ('onecolscrollersection', wagtail.blocks.StructBlock([('sidetitle', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('subtitle', wagtail.blocks.CharBlock(form_classname='subtitle', required=True)), ('btntitle', wagtail.blocks.CharBlock(form_classname='subtitle', required=True)), ('content', wagtail.blocks.CharBlock(form_classname='subtitle', required=True)), ('cards', wagtail.blocks.StreamBlock([('image', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(required=True))]))])), ('url', wagtail.blocks.URLBlock(form_classname='link', required=True)), ('btntext', wagtail.blocks.CharBlock(form_classname='subtitle', required=True))])), ('BenifitsBlock', wagtail.blocks.StructBlock([('sidetitle', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('subtitle', wagtail.blocks.CharBlock(form_classname='subtitle', required=True)), ('cards', wagtail.blocks.StreamBlock([('Benifitcard', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('subtitle', wagtail.blocks.CharBlock(form_classname='subtitle', required=True))]))]))]))], null=True),
        ),
        migrations.AlterField(
            model_name='contactuspage',
            name='body',
            field=wagtail.fields.StreamField([('herosection', wagtail.blocks.StructBlock([('sidetitle', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('content', wagtail.blocks.StreamBlock([('herocontent', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('subtitle', wagtail.blocks.CharBlock(form_classname='subtitle', required=True)), ('btn_title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('btn_icon', wagtail.images.blocks.ImageChooserBlock(required=False)), ('btn_link', wagtail.blocks.PageChooserBlock(can_choose_root=True)), ('include_fullimage', wagtail.blocks.BooleanBlock(required=False)), ('image_cover', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image_decor', wagtail.images.blocks.ImageChooserBlock(required=False))]))])), ('include_companies', wagtail.blocks.BooleanBlock(required=False)), ('company_image', wagtail.blocks.StreamBlock([('image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False))]))], required=False))])), ('ourmission', wagtail.blocks.StructBlock([('sidetitle', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('subtitle', wagtail.blocks.RichTextBlock(form_classname='subtitle', required=True)), ('cover_image', wagtail.images.blocks.ImageChooserBlock(required=False))])), ('ourvision', wagtail.blocks.StructBlock([('sidetitle', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('subtitle', wagtail.blocks.CharBlock(form_classname='subtitle', required=True)), ('cover_image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image1', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image2', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image3', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image4', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image5', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image6', wagtail.images.blocks.ImageChooserBlock(required=False))])), ('ourvalues', wagtail.blocks.StructBlock([('sidetitle', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('word1', wagtail.blocks.CharBlock(form_classname='word1', required=True)), ('word2', wagtail.blocks.CharBlock(form_classname='word2', required=True)), ('word3', wagtail.blocks.CharBlock(form_classname='word3', required=True)), ('word4', wagtail.blocks.CharBlock(form_classname='word4', required=True)), ('word5', wagtail.blocks.CharBlock(form_classname='word5', required=True))])), ('ourjourney', wagtail.blocks.StructBlock([('sidetitle', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('subtitle', wagtail.blocks.CharBlock(form_classname='subtitle', required=True)), ('ourjourneycards', wagtail.blocks.StreamBlock([('ourjourneycard', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('subtitle', wagtail.blocks.CharBlock(form_classname='subtitle', required=True))]))]))])), ('ourgallery', wagtail.blocks.StructBlock([('sidetitle', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('gallery', wagtail.blocks.StreamBlock([('gallery', wagtail.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock()))]))])), ('ourtestimonial', wagtail.blocks.StructBlock([('sidetitle', wagtail.blocks.CharBlock(form_classname='content', required=True)), ('name', wagtail.blocks.CharBlock(form_classname='content', required=True)), ('designation', wagtail.blocks.CharBlock(form_classname='content', required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('content', wagtail.blocks.CharBlock(form_classname='content', required=True)), ('svg', wagtail.images.blocks.ImageChooserBlock(required=False))])), ('blogsherosection', wagtail.blocks.StructBlock([('sidetitle', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('subtitle', wagtail.blocks.CharBlock(form_classname='subtitle', required=True)), ('cards', wagtail.blocks.StreamBlock([('blogsherosectioncards', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('subtitle', wagtail.blocks.CharBlock(form_classname='subtitle', required=True))]))]))])), ('coverImage', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False))])), ('culture', wagtail.blocks.StructBlock([('sidetitle', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('subtitle', wagtail.blocks.CharBlock(form_classname='subtitle', required=True)), ('gallery', wagtail.blocks.StreamBlock([('gallery', wagtail.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock()))]))])), ('onecolscrollersection', wagtail.blocks.StructBlock([('sidetitle', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('subtitle', wagtail.blocks.CharBlock(form_classname='subtitle', required=True)), ('btntitle', wagtail.blocks.CharBlock(form_classname='subtitle', required=True)), ('content', wagtail.blocks.CharBlock(form_classname='subtitle', required=True)), ('cards', wagtail.blocks.StreamBlock([('image', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(required=True))]))])), ('url', wagtail.blocks.URLBlock(form_classname='link', required=True)), ('btntext', wagtail.blocks.CharBlock(form_classname='subtitle', required=True))])), ('BenifitsBlock', wagtail.blocks.StructBlock([('sidetitle', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('subtitle', wagtail.blocks.CharBlock(form_classname='subtitle', required=True)), ('cards', wagtail.blocks.StreamBlock([('Benifitcard', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('subtitle', wagtail.blocks.CharBlock(form_classname='subtitle', required=True))]))]))])), ('OurworksHerosection', wagtail.blocks.StructBlock([('sidetitle', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('subtitle', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('content', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('primary_button', wagtail.blocks.StreamBlock([('button', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('icon', wagtail.images.blocks.ImageChooserBlock(required=False)), ('link', wagtail.blocks.PageChooserBlock(can_choose_root=True, required=False))]))])), ('image', wagtail.images.blocks.ImageChooserBlock(required=False))])), ('OurworksDisplay', wagtail.blocks.StructBlock([('sidetitle', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('subtitle', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('categorytitles', wagtail.blocks.StreamBlock([('TitleTabCombo', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(clasname='title', required=True)), ('tag', wagtail.blocks.ChoiceBlock(choices=[('csd-btn', 'Custom Sofware Development'), ('ui-btn', 'UI/UX Design'), ('all-btn', 'All')], icon='cup'))]))])), ('cards', wagtail.blocks.StreamBlock([('OurWorkCards', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(clasname='title', required=True)), ('tag', wagtail.blocks.ChoiceBlock(choices=[('csd', 'Custom Sofware Development'), ('ui', 'UI/UX Design')], icon='cup')), ('subtitle', wagtail.blocks.CharBlock(clasname='title', required=True)), ('label1', wagtail.blocks.CharBlock(clasname='data title 1', required=True)), ('label2', wagtail.blocks.CharBlock(clasname='data title 2', required=True)), ('data1', wagtail.blocks.CharBlock(clasname='data1', required=True)), ('data2', wagtail.blocks.CharBlock(clasname='data2', required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('bgcolor', wagtail.blocks.CharBlock(clasname='BackgroundColor', required=True))]))])), ('btntitle', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('icon', wagtail.images.blocks.ImageChooserBlock(required=False)), ('outlinegrey_button', wagtail.blocks.StreamBlock([('button', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('icon', wagtail.images.blocks.ImageChooserBlock(required=False)), ('link', wagtail.blocks.PageChooserBlock(can_choose_root=True, required=False))]))]))])), ('ContactusTesimonial', wagtail.blocks.StructBlock([('clutch_logo', wagtail.images.blocks.ImageChooserBlock(required=False)), ('testimonialcards', wagtail.blocks.StreamBlock([('testimonialcard', wagtail.blocks.StructBlock([('review', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('name', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('designation', wagtail.blocks.CharBlock(form_classname='title', required=True))]))]))]))], null=True),
        ),
        migrations.AlterField(
            model_name='ourworkspage',
            name='body',
            field=wagtail.fields.StreamField([('herosection', wagtail.blocks.StructBlock([('sidetitle', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('content', wagtail.blocks.StreamBlock([('herocontent', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('subtitle', wagtail.blocks.CharBlock(form_classname='subtitle', required=True)), ('btn_title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('btn_icon', wagtail.images.blocks.ImageChooserBlock(required=False)), ('btn_link', wagtail.blocks.PageChooserBlock(can_choose_root=True)), ('include_fullimage', wagtail.blocks.BooleanBlock(required=False)), ('image_cover', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image_decor', wagtail.images.blocks.ImageChooserBlock(required=False))]))])), ('include_companies', wagtail.blocks.BooleanBlock(required=False)), ('company_image', wagtail.blocks.StreamBlock([('image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False))]))], required=False))])), ('ourmission', wagtail.blocks.StructBlock([('sidetitle', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('subtitle', wagtail.blocks.RichTextBlock(form_classname='subtitle', required=True)), ('cover_image', wagtail.images.blocks.ImageChooserBlock(required=False))])), ('ourvision', wagtail.blocks.StructBlock([('sidetitle', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('subtitle', wagtail.blocks.CharBlock(form_classname='subtitle', required=True)), ('cover_image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image1', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image2', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image3', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image4', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image5', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image6', wagtail.images.blocks.ImageChooserBlock(required=False))])), ('ourvalues', wagtail.blocks.StructBlock([('sidetitle', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('word1', wagtail.blocks.CharBlock(form_classname='word1', required=True)), ('word2', wagtail.blocks.CharBlock(form_classname='word2', required=True)), ('word3', wagtail.blocks.CharBlock(form_classname='word3', required=True)), ('word4', wagtail.blocks.CharBlock(form_classname='word4', required=True)), ('word5', wagtail.blocks.CharBlock(form_classname='word5', required=True))])), ('ourjourney', wagtail.blocks.StructBlock([('sidetitle', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('subtitle', wagtail.blocks.CharBlock(form_classname='subtitle', required=True)), ('ourjourneycards', wagtail.blocks.StreamBlock([('ourjourneycard', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('subtitle', wagtail.blocks.CharBlock(form_classname='subtitle', required=True))]))]))])), ('ourgallery', wagtail.blocks.StructBlock([('sidetitle', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('gallery', wagtail.blocks.StreamBlock([('gallery', wagtail.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock()))]))])), ('ourtestimonial', wagtail.blocks.StructBlock([('sidetitle', wagtail.blocks.CharBlock(form_classname='content', required=True)), ('name', wagtail.blocks.CharBlock(form_classname='content', required=True)), ('designation', wagtail.blocks.CharBlock(form_classname='content', required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('content', wagtail.blocks.CharBlock(form_classname='content', required=True)), ('svg', wagtail.images.blocks.ImageChooserBlock(required=False))])), ('blogsherosection', wagtail.blocks.StructBlock([('sidetitle', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('subtitle', wagtail.blocks.CharBlock(form_classname='subtitle', required=True)), ('cards', wagtail.blocks.StreamBlock([('blogsherosectioncards', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('subtitle', wagtail.blocks.CharBlock(form_classname='subtitle', required=True))]))]))])), ('coverImage', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False))])), ('culture', wagtail.blocks.StructBlock([('sidetitle', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('subtitle', wagtail.blocks.CharBlock(form_classname='subtitle', required=True)), ('gallery', wagtail.blocks.StreamBlock([('gallery', wagtail.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock()))]))])), ('onecolscrollersection', wagtail.blocks.StructBlock([('sidetitle', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('subtitle', wagtail.blocks.CharBlock(form_classname='subtitle', required=True)), ('btntitle', wagtail.blocks.CharBlock(form_classname='subtitle', required=True)), ('content', wagtail.blocks.CharBlock(form_classname='subtitle', required=True)), ('cards', wagtail.blocks.StreamBlock([('image', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(required=True))]))])), ('url', wagtail.blocks.URLBlock(form_classname='link', required=True)), ('btntext', wagtail.blocks.CharBlock(form_classname='subtitle', required=True))])), ('BenifitsBlock', wagtail.blocks.StructBlock([('sidetitle', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('subtitle', wagtail.blocks.CharBlock(form_classname='subtitle', required=True)), ('cards', wagtail.blocks.StreamBlock([('Benifitcard', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('subtitle', wagtail.blocks.CharBlock(form_classname='subtitle', required=True))]))]))])), ('OurworksHerosection', wagtail.blocks.StructBlock([('sidetitle', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('subtitle', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('content', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('primary_button', wagtail.blocks.StreamBlock([('button', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('icon', wagtail.images.blocks.ImageChooserBlock(required=False)), ('link', wagtail.blocks.PageChooserBlock(can_choose_root=True, required=False))]))])), ('image', wagtail.images.blocks.ImageChooserBlock(required=False))])), ('OurworksDisplay', wagtail.blocks.StructBlock([('sidetitle', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('subtitle', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('categorytitles', wagtail.blocks.StreamBlock([('TitleTabCombo', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(clasname='title', required=True)), ('tag', wagtail.blocks.ChoiceBlock(choices=[('csd-btn', 'Custom Sofware Development'), ('ui-btn', 'UI/UX Design'), ('all-btn', 'All')], icon='cup'))]))])), ('cards', wagtail.blocks.StreamBlock([('OurWorkCards', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(clasname='title', required=True)), ('tag', wagtail.blocks.ChoiceBlock(choices=[('csd', 'Custom Sofware Development'), ('ui', 'UI/UX Design')], icon='cup')), ('subtitle', wagtail.blocks.CharBlock(clasname='title', required=True)), ('label1', wagtail.blocks.CharBlock(clasname='data title 1', required=True)), ('label2', wagtail.blocks.CharBlock(clasname='data title 2', required=True)), ('data1', wagtail.blocks.CharBlock(clasname='data1', required=True)), ('data2', wagtail.blocks.CharBlock(clasname='data2', required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('bgcolor', wagtail.blocks.CharBlock(clasname='BackgroundColor', required=True))]))])), ('btntitle', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('icon', wagtail.images.blocks.ImageChooserBlock(required=False)), ('outlinegrey_button', wagtail.blocks.StreamBlock([('button', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('icon', wagtail.images.blocks.ImageChooserBlock(required=False)), ('link', wagtail.blocks.PageChooserBlock(can_choose_root=True, required=False))]))]))])), ('TestimonialGeneric', wagtail.blocks.StructBlock([('sidetitle', wagtail.blocks.CharBlock(form_classname='content', required=True)), ('name', wagtail.blocks.CharBlock(form_classname='content', required=True)), ('designation', wagtail.blocks.CharBlock(form_classname='content', required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('content', wagtail.blocks.CharBlock(form_classname='content', required=True)), ('svg', wagtail.images.blocks.ImageChooserBlock(required=False)), ('bgcolor', wagtail.blocks.CharBlock(form_classname='bgcolor', required=True)), ('fontcolor', wagtail.blocks.CharBlock(form_classname='bgcolor', required=True))]))], null=True),
        ),
        migrations.AlterField(
            model_name='thankyoupage',
            name='body',
            field=wagtail.fields.StreamField([('herosection', wagtail.blocks.StructBlock([('sidetitle', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('content', wagtail.blocks.StreamBlock([('herocontent', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('subtitle', wagtail.blocks.CharBlock(form_classname='subtitle', required=True)), ('btn_title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('btn_icon', wagtail.images.blocks.ImageChooserBlock(required=False)), ('btn_link', wagtail.blocks.PageChooserBlock(can_choose_root=True)), ('include_fullimage', wagtail.blocks.BooleanBlock(required=False)), ('image_cover', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image_decor', wagtail.images.blocks.ImageChooserBlock(required=False))]))])), ('include_companies', wagtail.blocks.BooleanBlock(required=False)), ('company_image', wagtail.blocks.StreamBlock([('image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False))]))], required=False))])), ('ourmission', wagtail.blocks.StructBlock([('sidetitle', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('subtitle', wagtail.blocks.RichTextBlock(form_classname='subtitle', required=True)), ('cover_image', wagtail.images.blocks.ImageChooserBlock(required=False))])), ('ourvision', wagtail.blocks.StructBlock([('sidetitle', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('subtitle', wagtail.blocks.CharBlock(form_classname='subtitle', required=True)), ('cover_image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image1', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image2', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image3', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image4', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image5', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image6', wagtail.images.blocks.ImageChooserBlock(required=False))])), ('ourvalues', wagtail.blocks.StructBlock([('sidetitle', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('word1', wagtail.blocks.CharBlock(form_classname='word1', required=True)), ('word2', wagtail.blocks.CharBlock(form_classname='word2', required=True)), ('word3', wagtail.blocks.CharBlock(form_classname='word3', required=True)), ('word4', wagtail.blocks.CharBlock(form_classname='word4', required=True)), ('word5', wagtail.blocks.CharBlock(form_classname='word5', required=True))])), ('ourjourney', wagtail.blocks.StructBlock([('sidetitle', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('subtitle', wagtail.blocks.CharBlock(form_classname='subtitle', required=True)), ('ourjourneycards', wagtail.blocks.StreamBlock([('ourjourneycard', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('subtitle', wagtail.blocks.CharBlock(form_classname='subtitle', required=True))]))]))])), ('ourgallery', wagtail.blocks.StructBlock([('sidetitle', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('gallery', wagtail.blocks.StreamBlock([('gallery', wagtail.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock()))]))])), ('ourtestimonial', wagtail.blocks.StructBlock([('sidetitle', wagtail.blocks.CharBlock(form_classname='content', required=True)), ('name', wagtail.blocks.CharBlock(form_classname='content', required=True)), ('designation', wagtail.blocks.CharBlock(form_classname='content', required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('content', wagtail.blocks.CharBlock(form_classname='content', required=True)), ('svg', wagtail.images.blocks.ImageChooserBlock(required=False))])), ('blogsherosection', wagtail.blocks.StructBlock([('sidetitle', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('subtitle', wagtail.blocks.CharBlock(form_classname='subtitle', required=True)), ('cards', wagtail.blocks.StreamBlock([('blogsherosectioncards', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('subtitle', wagtail.blocks.CharBlock(form_classname='subtitle', required=True))]))]))])), ('coverImage', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False))])), ('culture', wagtail.blocks.StructBlock([('sidetitle', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('subtitle', wagtail.blocks.CharBlock(form_classname='subtitle', required=True)), ('gallery', wagtail.blocks.StreamBlock([('gallery', wagtail.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock()))]))])), ('onecolscrollersection', wagtail.blocks.StructBlock([('sidetitle', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('subtitle', wagtail.blocks.CharBlock(form_classname='subtitle', required=True)), ('btntitle', wagtail.blocks.CharBlock(form_classname='subtitle', required=True)), ('content', wagtail.blocks.CharBlock(form_classname='subtitle', required=True)), ('cards', wagtail.blocks.StreamBlock([('image', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(required=True))]))])), ('url', wagtail.blocks.URLBlock(form_classname='link', required=True)), ('btntext', wagtail.blocks.CharBlock(form_classname='subtitle', required=True))])), ('BenifitsBlock', wagtail.blocks.StructBlock([('sidetitle', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('subtitle', wagtail.blocks.CharBlock(form_classname='subtitle', required=True)), ('cards', wagtail.blocks.StreamBlock([('Benifitcard', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('subtitle', wagtail.blocks.CharBlock(form_classname='subtitle', required=True))]))]))])), ('OurworksHerosection', wagtail.blocks.StructBlock([('sidetitle', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('subtitle', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('content', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('primary_button', wagtail.blocks.StreamBlock([('button', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('icon', wagtail.images.blocks.ImageChooserBlock(required=False)), ('link', wagtail.blocks.PageChooserBlock(can_choose_root=True, required=False))]))])), ('image', wagtail.images.blocks.ImageChooserBlock(required=False))])), ('OurworksDisplay', wagtail.blocks.StructBlock([('sidetitle', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('subtitle', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('categorytitles', wagtail.blocks.StreamBlock([('TitleTabCombo', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(clasname='title', required=True)), ('tag', wagtail.blocks.ChoiceBlock(choices=[('csd-btn', 'Custom Sofware Development'), ('ui-btn', 'UI/UX Design'), ('all-btn', 'All')], icon='cup'))]))])), ('cards', wagtail.blocks.StreamBlock([('OurWorkCards', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(clasname='title', required=True)), ('tag', wagtail.blocks.ChoiceBlock(choices=[('csd', 'Custom Sofware Development'), ('ui', 'UI/UX Design')], icon='cup')), ('subtitle', wagtail.blocks.CharBlock(clasname='title', required=True)), ('label1', wagtail.blocks.CharBlock(clasname='data title 1', required=True)), ('label2', wagtail.blocks.CharBlock(clasname='data title 2', required=True)), ('data1', wagtail.blocks.CharBlock(clasname='data1', required=True)), ('data2', wagtail.blocks.CharBlock(clasname='data2', required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('bgcolor', wagtail.blocks.CharBlock(clasname='BackgroundColor', required=True))]))])), ('btntitle', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('icon', wagtail.images.blocks.ImageChooserBlock(required=False)), ('outlinegrey_button', wagtail.blocks.StreamBlock([('button', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('icon', wagtail.images.blocks.ImageChooserBlock(required=False)), ('link', wagtail.blocks.PageChooserBlock(can_choose_root=True, required=False))]))]))])), ('ContactusTesimonial', wagtail.blocks.StructBlock([('clutch_logo', wagtail.images.blocks.ImageChooserBlock(required=False)), ('testimonialcards', wagtail.blocks.StreamBlock([('testimonialcard', wagtail.blocks.StructBlock([('review', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('name', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('designation', wagtail.blocks.CharBlock(form_classname='title', required=True))]))]))])), ('thankyoublock', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('subtitle', wagtail.blocks.CharBlock(form_classname='subtitle', required=True)), ('image_cover', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image_decor', wagtail.images.blocks.ImageChooserBlock(required=False))]))], null=True),
        ),
    ]
