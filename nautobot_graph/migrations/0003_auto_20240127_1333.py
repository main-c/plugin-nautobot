# Generated by Django 3.2.23 on 2024-01-27 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nautobot_graph', '0002_auto_20240127_0702'),
    ]

    operations = [
        migrations.AddField(
            model_name='relationshiptype',
            name='dst_node_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dst_relationships', to='nautobot_graph.nodetype'),
        ),
        migrations.AddField(
            model_name='relationshiptype',
            name='src_node_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='src_relationships', to='nautobot_graph.nodetype'),
        ),
        migrations.AlterUniqueTogether(
            name='nodeproperty',
            unique_together={('name', 'node_type')},
        ),
        migrations.AlterUniqueTogether(
            name='relationshipproperty',
            unique_together={('name', 'relationship_type')},
        ),
    ]
