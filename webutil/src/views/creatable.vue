<template>
	<div>
		<div>
			<top></top>
			<div class="top">
			<div style="flex: 2;padding: 5px;">
				<el-input v-model="ztablename" placeholder="中文表名"></el-input>
			</div>
			<div style="flex: 2;padding: 5px;">
				<el-input v-model="tablename" placeholder="英文表名"></el-input>
			</div>
			<div style="flex: 3;padding: 5px;">
				<el-select v-model="value" clearable placeholder="请选择行业名称">
					<el-option v-for="item in options" :key="item.value" :label="item.label" :value="item.value">
					</el-option>
				</el-select>
			</div>
			<div style="flex: 3;line-height: 50px;">
				<el-button style="width: 120px;" type="primary" @click="constructdatabase()"  >查看表结构</el-button>&nbsp;&nbsp;&nbsp;&nbsp;
				<el-button style="width: 120px;" type="primary" @click="searchdatabase()"  >查看表存在</el-button>&nbsp;&nbsp;&nbsp;&nbsp;
				<router-link to="/tabledetail"><span style="color: #1989fa;font-weight: bold;">查看已保存</span></router-link>
			</div>
		</div>
			<div style="flex: 1;padding-right: 20px;margin-top: 20px;">
				<el-input type="textarea" :rows="16" placeholder="请输入字段名 字段中文名 字段类型 是否主键 是否可空以空格隔开,每行以中文句号结尾" v-model="ctable">
				</el-input>
			</div>
			<div style="padding: 15px;text-align: center;">
				<el-button style="width: 100px;" type="primary" @click="sub()">提交</el-button>&nbsp;&nbsp;&nbsp;&nbsp;
				<el-button style="width: 100px;" type="danger" @click="clear()">清空</el-button>
			</div>
		</div>
		<div style="padding: 10px;">
			<p>{{rdata}}</p>
		</div>
		<div v-show="isshow" style="text-align: center;">
			<el-button style="width: 100px;" type="primary" @click="save()">保存</el-button>&nbsp;&nbsp;&nbsp;&nbsp;
			<el-button style="width: 100px;" type="primary" @click="savedatabase()">物理表</el-button>&nbsp;&nbsp;&nbsp;&nbsp;

		</div>
		<div style="margin-top: 20px;padding: 20px;" v-show="res!=''">
			<br /><br />
			<div>
				<el-table :data="res.result" border>
					<el-table-column :label="val" v-for="(val, i) in res.title" :key="i">
						<template slot-scope="scope">{{res.result[scope.$index][i]}}</template>
					</el-table-column>
				</el-table>
			</div>
		</div>
		<!-- // let word = "select count(*) from pg_class where relname = '"+this.tablename+"';" -->
		<div style="height: 100px;">

		</div>
		<foot></foot>
	</div>
</template>

<script>
	import top from '../components/top.vue'
	import foot from '../components/footer.vue'
	export default{
		name:'createtable',
		data(){
			return{
				options: [{
				 	value: '国民经济核算',
						label: '国民经济核算'
					}, {
						value: '固定资产投资',
						label: '固定资产投资'
					}, {
						value: '对外经济贸易',
						label: '对外经济贸易'
					}, {
						value: '价格',
						label: '价格'
					}, {
						value: '财政',
						label: '财政'
					},
					{
						value: '金融业',
						label: '金融业'
					},
					{
						value: '保险业',
						label: '保险业'
					},
					{
						value: '农业',
						label: '农业'
					},
					{
						value: '工业',
						label: '工业'
					},
					{
						value: '建筑业',
						label: '建筑业'
					}, {
						value: '科技',
						label: '科技'
					}, {
						value: '能源',
						label: '能源'
					}, {
						value: '交通运输',
						label: '交通运输'
					}, {
						value: '房地产',
						label: '房地产'
					}, {
						value: '批发与零售',
						label: '批发与零售'
					}, {
						value: '经济安全保障',
						label: '经济安全保障'
					}, {
						value: '人口',
						label: '人口'
					},
					{
						value: '就业人员和工资',
						label: '就业人员和工资'
					}, {
						value: '人民生活',
						label: '人民生活'
					}, {
						value: '生态环境保护',
						label: '生态环境保护'
					}, {
						value: '绿色生态',
						label: '绿色生态'
					}, {
						value: '邮电和软件业',
						label: '邮电和软件业'
					}, {
						value: '住宿和餐饮业',
						label: '住宿和餐饮业'
					}, {
						value: '旅游业',
						label: '旅游业'
					}, {
						value: '教育',
						label: '教育'
					}, {
						value: '社会服务',
						label: '社会服务'
					}
				],
				value: '',
				hangye:'',
				ztablename:'',
				tablename:'',
				ctable:'',
				rdata:'',
				isshow:false,
				res:''
			}
		},
		components:{
			top,
			foot
		},
		methods:{
			sub(){
				let data = {
					tablename:this.tablename,
					ztablename:this.ztablename,
					hangye:this.hangye,
					data :this.ctable
				}
				this.$axios.post(this.$https+"/createtable",this.$qs.stringify(data)).then(res=>{
					this.rdata = res.data.data
					this.isshow =true
				}).catch(res=>{
					console(res)
				})
			},
			clear(){
				this.tablename = ''
				this.ctable = ''
				this.rdata = ''
				this.ztablename = ''
				this.hangye = ''
				this.res = ''
				this.isshow = false
			},
			save(){
				let data = {
					tablename:this.tablename,
					ztablename:this.ztablename,
					hangye:this.value,
					data:this.rdata
				}
				this.$axios.post(this.$https+"/savetable",this.$qs.stringify(data)).then(res=>{
					console.log(res)
					if(res.status==200){
							this.$message({ message:'保存成功！',type: 'success'});
					}else{
						this.$message.error( '保存失败！');
					}
				}).catch(res=>{

				})
			},
			savedatabase(){
				let word = ''
				let data = {
					sql:word+this.rdata
				}
				this.$axios.post(this.$https+"/savedatabase",this.$qs.stringify(data)).then(res=>{
					console.log(res.data)
					if(res.status==200){
						this.$message({ message:'执行成功！',type: 'success'});
					}else{
						this.$message.error( '保存失败！');
					}
				}).catch(res=>{
					console(res)
				})
			},
			searchdatabase(){
				let word = "select count(*) from pg_class where relname = '"+this.tablename+"';"
				let data = {
					sql:word
				}
				this.$axios.post(this.$https+"/savedatabase",this.$qs.stringify(data)).then(res=>{
					this.res = res.data
					console.log(res.data)
					if(this.res.result[0]==1){
						this.$message({ message:'该表存在',type: 'success'})
					}else{
						this.$message({ message:'该表不存在',type: 'error'})
					}
				}).catch(res=>{
					console(res)
				})
			},
			constructdatabase(){
				let word = "select a.attnum AS 序号,c.relname AS 表名,cast(obj_description(c.oid) AS varchar) AS 表名描述,a.attname AS 列名,t.typname AS 字段类型,CASE WHEN t.typlen = -1 THEN a.atttypmod - 4 ELSE t.typlen::integer END AS 字段大小 ,d.description AS 备注 from pg_attribute a left join pg_description d on d.objoid = a.attrelid and d.objsubid = a.attnum left join pg_class c on a.attrelid = c.oid left join pg_type t on a.atttypid = t.oid where a.attnum >= 0 and c.relname like   '"+ this.tablename +"'   order by c.relname desc,a.attnum asc;"
				let data = {
					sql:word
				}
				this.$axios.post(this.$https+"/savedatabase",this.$qs.stringify(data)).then(res=>{
					this.res = res.data
				}).catch(res=>{
					console(res)
				})
			}


		}
	}
</script>

<style scoped>
	.top {
		display: flex;
		margin-top: 50px;
	}
</style>
